# -*- coding: utf-8 -*-
"""
This script is broken into three parts
1) Item name collection
    • Get the name of every item on the steam market place for a given game
2) Item price data collection
    • Loop through the item names to get the price history for each item
3) Data analysis
"""

import requests  # make http requests
import json  # make sense of what the requests return
import pickle  # save our data to our computer

import pandas as pd  # structure out data
import numpy as np  # do a bit of math
import scipy.stats as sci  # do a bit more math

from datetime import datetime  # make working with dates 1000x easier
import time  # become time lords
import random  # create random numbers (probably not needed)

# Login to steam on your browser and get your steam login cookie
# For Chrome, settings > advanced > content settings > cookies > see all cookies and site data > find steamcommunity.com > find "steamLoginSecure" > copy the "Content" string and paste below
cookie = {'steamLoginSecure': '123451234512345%ABC%ABC%123%123456ABC12345'};

# gameList as a string or list of strings
# rust, 252490, dota2, 570; CSGO, 730; pubg, 578080; TF2, 440;
# you can find the app id by going to the community market and finding the appid=##### in the URL
gameList = ['252490', '578080'];

for gameID in gameList:
    # itialize
    allItemNames = [];

    # find total number items
    allItemsGet = requests.get(
        'https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=default&sort_dir=desc&appid=' + gameID + '&norender=1&count=100',
        cookies=cookie);  # get page
    allItems = allItemsGet.content;  # get page content

    allItems = json.loads(allItems);  # convert to JSON
    totalItems = allItems['total_count'];  # get total count

    # you can only get 100 items at a time (despite putting in count= >100)
    # so we have to loop through in batches of 100 to get every single item name by specifying the start position
    for currPos in range(0, totalItems + 100, 100):  # loop through all items
        time.sleep(random.uniform(0.5, 2.5))  # you cant make requests too quickly or steam gets mad

        # get item name of each
        allItemsGet = requests.get('https://steamcommunity.com/market/search/render/?start=' + str(
            currPos) + '&count=100&search_descriptions=0&sort_column=default&sort_dir=desc&appid=' + gameID + '&norender=1&count=5000',
                                   cookies=cookie);
        print('Items ' + str(currPos) + ' out of ' + str(totalItems) + ' code: ' + str(
            allItemsGet.status_code))  # reassure us the code is running and we are getting good returns (code 200)

        allItems = allItemsGet.content;
        allItems = json.loads(allItems);
        allItems = allItems['results'];
        for currItem in allItems:
            allItemNames.append(currItem['hash_name'])  # save the names

    # remove dupes by converting from list to set and back again
    allItemNames = list(set(allItemNames))

    # Save all the name so we don't have to do this step anymore
    # use pickle to save all the names so i dont have to keep running above code
    with open(gameID + 'ItemNames.txt', "wb") as file:  # change the text file name to whatever you want
        pickle.dump(allItemNames, file)

    """
    ~*~*~*~*~*~*~*~*~*~*~*~

    Step 2: Data collection

    ~*~*~*~*~*~*~*~*~*~*~*~
    don't forget to import libraries if you start here
    """
for gameID in gameList:
    # open file with all names
    with open(gameID + 'ItemNames.txt', "rb") as file:  # Unpickling
        allItemNames = pickle.load(file)

    # intialize our Panda's dataframe with the data we want from each item
    allItemsPD = pd.DataFrame(data=None, index=None,
                              columns=['itemName', 'initial', 'timeOnMarket', 'priceIncrease', 'priceAvg', 'priceSD',
                                       'maxPrice', 'maxIdx', 'minPrice', 'minIdx', 'swing', 'volAvg', 'volSD', 'slope',
                                       'rr']);
    currRun = 1;  # to keep track of the program running

    for currItem in allItemNames:  # go through all item names
        # need to encode symbols into ASCII for http (https://www.w3schools.com/tags/ref_urlencode.asp)
        currItemHTTP = currItem.replace(' ', '%20');  # convert spaces to %20
        currItemHTTP = currItemHTTP.replace('&', '%26');  # convert & to %26
        # I was lazy there's probably others but I catch this below
        item = requests.get(
            'https://steamcommunity.com/market/pricehistory/?appid=' + gameID + '&market_hash_name=' + currItemHTTP,
            cookies=cookie);  # get item data
        print(str(currRun), ' out of ', str(len(allItemNames)) + ' code: ' + str(item.status_code));
        currRun += 1;
        item = item.content;
        item = json.loads(item);
        if item:  # did we even get any data back
            itemPriceData = item['prices']  # is there price data?
            if itemPriceData == False or not itemPriceData:  # if there was an issue with the request then data will return false and the for loop will just continue to the next item
                continue  # this could be cause the http item name was weird (eg symbol not converted to ASCII) but it will also occur if you make too many requests too fast (this is handled below)
            else:
                # initialize stuff
                itemPrices = [];  # steam returns MEDIAN price for given time bin
                itemVol = [];
                itemDate = [];
                for currDay in itemPriceData:  # pull out the actual data
                    itemPrices.append(currDay[1]);  # idx 1 is price
                    itemVol.append(currDay[2]);  # idx 2 is volume of items sold
                    itemDate.append(datetime.strptime(currDay[0][0:11], '%b %d %Y'))  # idx 0 is the date

                # lists are strings, convert to numbers
                itemPrices = list(map(float, itemPrices));
                itemVol = list(map(int, itemVol));

                # combine sales that occurs on the same day
                # avg prices, sum volume
                # certainly not the best way to do this but, whatever
                for currDay in range(len(itemDate) - 1, 1, -1):  # start from end (-1) and go to start
                    if itemDate[currDay] == itemDate[
                        currDay - 1]:  # if current element's date same as the one before it
                        itemPrices[currDay - 1] = np.mean(
                            [itemPrices[currDay], itemPrices[currDay - 1]]);  # average prices from the two days
                        itemVol[currDay - 1] = np.sum([itemVol[currDay], itemVol[currDay - 1]]);  # sum volume
                        # delete the repeats
                        del itemDate[currDay]
                        del itemVol[currDay]
                        del itemPrices[currDay]

                # now that days are combined
                normTime = list(range(0,
                                      len(itemPrices)));  # create a new list that "normalizes" days from 0 to n, easier to work with than datetime

                # some basic data
                timeOnMarket = (datetime.today() - itemDate[
                    0]).days;  # have to do this because if sales are spare day[0] could be months/years ago
                priceIncrease = itemPrices[-1] - itemPrices[
                    0];  # what was the price increase from day 0 to the most recent day [-1]
                maxPrice = max(itemPrices);  # max price
                maxIdx = itemPrices.index(maxPrice);  # when was the max price?
                minPrice = min(itemPrices);
                minIdx = itemPrices.index(minPrice);
                swing = maxPrice - minPrice;  # greatest price swing

                # get some descriptive stats
                itemPriceAvg = np.mean(itemPrices);  # average price
                if len(itemPrices) > 1:  # make sure there is at least two days of sales
                    itemPriceInitial = itemPrices[1] - itemPrices[
                        0];  # how much did the price jump from day 0 to 1? eg the first trading day
                else:
                    itemPriceInitial = itemPrices[0];
                itemVolAvg = np.mean(itemVol);

                itemPriceSD = np.std(itemPrices);
                itemVolSD = np.std(itemVol);

                # linear regression to find slope and fit
                fitR = sci.linregress(normTime, itemPrices);  # slope intercept rvalue pvalue stderr
                RR = float(fitR[2] ** 2);  # convert to R^2 value

                # save data
                currentItemDict = {'itemName': currItem, 'initial': itemPriceInitial, 'timeOnMarket': timeOnMarket,
                                   'priceIncrease': priceIncrease, 'priceAvg': itemPriceAvg, 'priceSD': itemPriceSD,
                                   'maxPrice': maxPrice, 'maxIdx': maxIdx, 'minPrice': minPrice, 'minIdx': minIdx,
                                   'swing': swing, 'volAvg': itemVolAvg, 'volSD': itemVolSD, 'slope': fitR[0], 'rr': RR}
                currItemPD = pd.DataFrame(currentItemDict, index=[0]);
                allItemsPD = allItemsPD.append(currItemPD, ignore_index=True);

                time.sleep(random.uniform(0.5, 2.5))
        else:
            continue
print('All item data collected')

# save the dataframe
allItemsPD.to_pickle(gameID + 'PriceData.pkl');

"""
~*~*~*~*~*~*~*~*~*~*~*~

Step 3: Data analysis

~*~*~*~*~*~*~*~*~*~*~*~
    don't forget to import libraries if you start here
"""
gameID = '578080';
# open file with all names
with open(gameID + 'PriceData.pkl', "rb") as file:  # Unpickling
    data = pickle.load(file)

