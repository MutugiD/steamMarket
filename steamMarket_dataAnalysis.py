# -*- coding: utf-8 -*-
"""
pickle files in a seperate dir
"""
import pandas as pd
import numpy as np
import scipy.stats as sci
import pickle
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import seaborn as sns
import ptitprince as pt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from statsmodels.stats.multicomp import pairwise_tukeyhsd

gameID = '252490';
# open file with all names
with open(gameID + 'PriceData_master_priceFill.pkl', "rb") as file:  # Unpickling
    data = pickle.load(file)

with open(gameID + 'PriceData_3.pkl', "rb") as file:  # Unpickling
    combo = pickle.load(file)

with open(gameID + 'PriceData_2.pkl', "rb") as file:  # Unpickling
    combo2 = pickle.load(file)

with open(gameID + 'marketDelta.pkl', "rb") as file:  # Unpickling
    marketDelta = pickle.load(file)

with open(gameID + 'marketPrice.pkl', "rb") as file:  # Unpickling
    marketPrice = pickle.load(file)

with open(gameID + 'marketVol.pkl', "rb") as file:  # Unpickling
    marketVol = pickle.load(file)

roughConversion = 1.49;

# with open(gameID+'PriceData_backUp_manualPrices09032019.pkl', "rb") as file:   # Unpickling
#   data = pickle.load(file)

# convert these from datetimes and indexes to numbers
data['timeOnMarket'] = pd.to_numeric(data['timeOnMarket']);
data['maxIdx'] = pd.to_numeric(data['maxIdx']);
data['minIdx'] = pd.to_numeric(data['minIdx']);
data['tier'] = pd.to_numeric(data['tier']);
data['OG_price'] = pd.to_numeric(data['OG_price']);
data['itemName'] = data['itemName'].str.lower();
data['itemTypeGeneral'] = "";
data['tier'] = "";
data['OG_price_NZ'] = data['OG_price'] * roughConversion;

data = data[
    ['tier', 'itemTypeGeneral', 'itemType', 'OG_price', 'OG_price_NZ', 'initial', 'timeOnMarket', 'priceAvg', 'priceSD',
     'priceIncrease', 'smoothChange', 'maxPrice', 'maxIdx', 'minPrice', 'minIdx', 'maxMinIdxDiff', 'swing', 'volAvg',
     'volSD', 'slope', 'rr']];

# for currName in data.loc[:,'itemName']:
#
test['OG_price'][test['itemType'].str.contains('ak47') & test['OG_price'].isnull()] = 1.99;

uniqueItems = data.itemType.unique().tolist();

for currItem in uniqueItems:
    data['OG_price'][data['itemType'].str.contains(currItem) & data['OG_price'].isnull()] = np.mean(
        data['OG_price'][data['itemType'].str.contains(currItem) & data['OG_price'].notnull()]);

data['OG_to_avg'] = data['priceAvg'] - data['OG_price_NZ'];

data['itemTypeGeneral'][data['itemName'].str.contains('hat')] = 'clothing';

data['itemTypeGeneral'][data['itemName'].str.contains('guitar')] = 'RP';
data['itemTypeGeneral'][data['itemName'].str.contains('box')] = 'RP';
data['itemTypeGeneral'][data['itemName'].str.contains('trunk')] = 'RP';
data['itemTypeGeneral'][data['itemName'].str.contains('storage')] = 'RP';
data['itemTypeGeneral'][data['itemName'].str.contains('door')] = 'RP';
data['itemTypeGeneral'][data['itemName'].str.contains('bag')] = 'RP';
data['itemTypeGeneral'][data['itemName'].str.contains('furnace')] = 'RP';
data['itemTypeGeneral'][data['itemName'].str.contains('fridge')] = 'RP';
data['itemTypeGeneral'][data['itemName'].str.contains('locker')] = 'RP';
data['itemTypeGeneral'][data['itemName'].str.contains('carpet')] = 'RP';
data['itemTypeGeneral'][data['itemName'].str.contains('rug')] = 'RP';
data['itemTypeGeneral'][data['itemName'].str.contains('bed')] = 'RP';
data['itemTypeGeneral'][data['itemName'].str.contains('machine')] = 'RP';
data['itemTypeGeneral'][data['itemName'].str.contains('chair')] = 'RP';
data['itemTypeGeneral'][data['itemName'].str.contains('table')] = 'RP';
data['itemTypeGeneral'][data['itemName'].str.contains('barricade')] = 'RP';

data['itemTypeGeneral'][data['itemName'].str.contains('hatchet')] = 'tool';
data['itemTypeGeneral'][data['itemName'].str.contains('pickaxe')] = 'tool';
data['itemTypeGeneral'][data['itemName'].str.contains('axe')] = 'tool';
data['itemTypeGeneral'][data['itemName'].str.contains('hammer')] = 'tool';
data['itemTypeGeneral'][data['itemName'].str.contains('pick')] = 'tool';
data['itemTypeGeneral'][data['itemName'].str.contains('rock')] = 'tool';

data['itemTypeGeneral'][data['itemName'].str.contains('sword')] = 'melee';
data['itemTypeGeneral'][data['itemName'].str.contains('club')] = 'melee';
data['itemTypeGeneral'][data['itemName'].str.contains('blade')] = 'melee';
data['itemTypeGeneral'][data['itemName'].str.contains('knife')] = 'melee';

data['itemTypeGeneral'][data['itemName'].str.contains('shotgun')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('dbs')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('pump')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('python')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('mp5')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('sar')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('rifle')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('pistol')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('revolver')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('smg')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('ak47')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('sap')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('smg')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('gun')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('bolt')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('47')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('bar')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('300')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('eoka')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains('pipe')] = 'gun';
data['itemTypeGeneral'][data['itemName'].str.contains(' ak')] = 'gun';

data['itemTypeGeneral'][data['itemName'].str.contains('grenade')] = 'explosive';
data['itemTypeGeneral'][data['itemName'].str.contains('satchel')] = 'explosive';
data['itemTypeGeneral'][data['itemName'].str.contains('rocket')] = 'explosive';
data['itemTypeGeneral'][data['itemName'].str.contains('launcher')] = 'explosive';

data['itemTypeGeneral'][data['itemName'].str.contains('crossbow')] = 'crossbow';
data['itemTypeGeneral'][data['itemType'].str.contains('crossbow')] = 'gun';

data['itemTypeGeneral'][data['itemName'].str.contains('hoodie')] = 'clothing';
data['itemTypeGeneral'][data['itemName'].str.contains('shirt')] = 'clothing';
data['itemTypeGeneral'][data['itemName'].str.contains('gloves')] = 'clothing';
data['itemTypeGeneral'][data['itemName'].str.contains('pants')] = 'clothing';
data['itemTypeGeneral'][data['itemName'].str.contains('bandana')] = 'clothing';
data['itemTypeGeneral'][data['itemName'].str.contains('vest')] = 'clothing';
data['itemTypeGeneral'][data['itemName'].str.contains('boots')] = 'clothing';
data['itemTypeGeneral'][data['itemName'].str.contains('boonie')] = 'clothing';
data['itemTypeGeneral'][data['itemName'].str.contains('cap')] = 'clothing';
data['itemTypeGeneral'][data['itemName'].str.contains('shoes')] = 'clothing';
data['itemTypeGeneral'][data['itemName'].str.contains('jacket')] = 'clothing';
data['itemTypeGeneral'][data['itemName'].str.contains('balaclava')] = 'clothing';
data['itemTypeGeneral'][data['itemName'].str.contains('beenie')] = 'clothing';
data['itemTypeGeneral'][data['itemName'].str.contains('shorts')] = 'clothing';
data['itemTypeGeneral'][data['itemName'].str.contains('headwrap')] = 'clothing';

data['itemTypeGeneral'][data['itemName'].str.contains('poncho')] = 'armor';
data['itemTypeGeneral'][data['itemName'].str.contains('helmet')] = 'armor';
data['itemTypeGeneral'][data['itemName'].str.contains('chest')] = 'armor';
data['itemTypeGeneral'][data['itemName'].str.contains('mask')] = 'armor';
data['itemTypeGeneral'][data['itemName'].str.contains('kilt')] = 'armor';
data['itemTypeGeneral'][data['itemName'].str.contains('bucket')] = 'armor';

######################

data['tier'][data['itemName'].str.contains('hat')] = 0;
data['tier'][data['itemName'].str.contains('hatchet')] = 1;
data['tier'][data['itemName'].str.contains(' ak')] = 3;

data['tier'][data['itemName'].str.contains('guitar')] = 0;
data['tier'][data['itemName'].str.contains('box')] = 0;
data['tier'][data['itemName'].str.contains('trunk')] = 0;
data['tier'][data['itemName'].str.contains('storage')] = 0;
data['tier'][data['itemName'].str.contains('door')] = 0;
data['tier'][data['itemName'].str.contains('armored')] = 3;
data['tier'][data['itemName'].str.contains('bag')] = 0;
data['tier'][data['itemName'].str.contains('furnace')] = 0;
data['tier'][data['itemName'].str.contains('fridge')] = 1;
data['tier'][data['itemName'].str.contains('locker')] = 2;
data['tier'][data['itemName'].str.contains('carpet')] = 0;
data['tier'][data['itemName'].str.contains('rug')] = 0;
data['tier'][data['itemName'].str.contains('bed')] = 1;
data['tier'][data['itemName'].str.contains('machine')] = 1;
data['tier'][data['itemName'].str.contains('chair')] = 1;
data['tier'][data['itemName'].str.contains('table')] = 0;
data['tier'][data['itemName'].str.contains('barricade')] = 2;
data['tier'][data['itemName'].str.contains('garage')] = 1;

data['tier'][data['itemName'].str.contains('hammer')] = 0;
data['tier'][data['itemName'].str.contains('rock')] = 0;

data['tier'][data['itemName'].str.contains('club')] = 0;
data['tier'][data['itemName'].str.contains('knife')] = 0;

data['tier'][data['itemName'].str.contains('dbs')] = 1;
data['tier'][data['itemName'].str.contains('pump')] = 2;
data['tier'][data['itemName'].str.contains('python')] = 2;
data['tier'][data['itemName'].str.contains('mp5')] = 3;
data['tier'][data['itemName'].str.contains('sar')] = 2;
data['tier'][data['itemName'].str.contains('revolver')] = 1;
data['tier'][data['itemName'].str.contains('smg')] = 2;
data['tier'][data['itemName'].str.contains('ak47')] = 3;
data['tier'][data['itemName'].str.contains('sap')] = 2;
data['tier'][data['itemName'].str.contains('smg')] = 2;
data['tier'][data['itemName'].str.contains('bolt')] = 3;
data['tier'][data['itemName'].str.contains('47')] = 3;
data['tier'][data['itemName'].str.contains('bar')] = 3;
data['tier'][data['itemName'].str.contains('300')] = 4;
data['tier'][data['itemName'].str.contains('eoka')] = 0;
data['tier'][data['itemName'].str.contains('pipe')] = 1;

data['tier'][data['itemName'].str.contains('grenade')] = 2;
data['tier'][data['itemName'].str.contains('satchel')] = 2;
data['tier'][data['itemName'].str.contains('rocket')] = 3;
data['tier'][data['itemName'].str.contains('launcher')] = 3;

data['tier'][data['itemName'].str.contains('crossbow')] = 1;

data['tier'][data['itemName'].str.contains('hoodie')] = 2;
data['tier'][data['itemName'].str.contains('gloves')] = 0;
data['tier'][data['itemName'].str.contains('pants')] = 1;
data['tier'][data['itemName'].str.contains('bandana')] = 0;
data['tier'][data['itemName'].str.contains('boots')] = 2;
data['tier'][data['itemName'].str.contains('boonie')] = 0;
data['tier'][data['itemName'].str.contains('cap')] = 0;
data['tier'][data['itemName'].str.contains('shoes')] = 0;
data['tier'][data['itemName'].str.contains('jacket')] = 1;
data['tier'][data['itemName'].str.contains('balaclava')] = 0;
data['tier'][data['itemName'].str.contains('beenie')] = 0;
data['tier'][data['itemName'].str.contains('shorts')] = 0;
data['tier'][data['itemName'].str.contains('headwrap')] = 0;
data['tier'][data['itemName'].str.contains('shirt')] = 0;
data['tier'][data['itemName'].str.contains('shorts')] = 0;

data['tier'][data['itemName'].str.contains('poncho')] = 0;
data['tier'][data['itemName'].str.contains('chest plate')] = 3;
data['tier'][data['itemName'].str.contains('mask')] = 3;
data['tier'][data['itemName'].str.contains('kilt')] = 2;
data['tier'][data['itemName'].str.contains('bucket')] = 1;
data['tier'][data['itemName'].str.contains('roadsign')] = 2;
data['tier'][data['itemName'].str.contains('sign')] = 2;
data['tier'][data['itemName'].str.contains('vest')] = 2;

data['tier'][data['itemType'].str.contains('rs')] = 2;
data['tier'][data['itemType'].str.contains('vest')] = 2;

######

data['itemType'][data['itemName'].str.contains('hat')] = 'hat';
data['itemType'][data['itemName'].str.contains('hatchet')] = 'hatchet';
data['itemType'][data['itemName'].str.contains('stone hatchet')] = 'stone hatchet';
data['itemType'][data['itemName'].str.contains('axe')] = 'pickaxe';
data['itemType'][data['itemName'].str.contains('pickaxe')] = 'pickaxe';
data['itemType'][data['itemName'].str.contains('stone pickaxe')] = 'stone pickaxe';

data['itemType'][data['itemName'].str.contains('guitar')] = 'guitar';
data['itemType'][data['itemName'].str.contains('trunk')] = 'lw box';
data['itemType'][data['itemName'].str.contains('storage')] = 'lw box';
data['itemType'][data['itemName'].str.contains('wooden door')] = 'wooden door';
data['itemType'][data['itemName'].str.contains('bag')] = 'sleeping bag';
data['itemType'][data['itemName'].str.contains('furnace')] = 'furnace';
data['itemType'][data['itemName'].str.contains('fridge')] = 'fridge';
data['itemType'][data['itemName'].str.contains('locker')] = 'locker';
data['itemType'][data['itemName'].str.contains('carpet')] = 'rug';
data['itemType'][data['itemName'].str.contains('rug')] = 'rug';
data['itemType'][data['itemName'].str.contains('bed')] = 'bed';
data['itemType'][data['itemName'].str.contains('machine')] = 'vending';
data['itemType'][data['itemName'].str.contains('chair')] = 'chair';
data['itemType'][data['itemName'].str.contains('table')] = 'table';
data['itemType'][data['itemName'].str.contains('barricade')] = 'barricade';
data['itemType'][data['itemName'].str.contains('garage')] = 'garage door';
data['itemType'][data['itemName'].str.contains('sheet metal door')] = 'sheet metal door';

data['itemType'][data['itemName'].str.contains('hammer')] = 'hammer';
data['itemType'][data['itemName'].str.contains('rock')] = 'rock';

data['itemType'][data['itemName'].str.contains('sword')] = 'sword';
data['itemType'][data['itemName'].str.contains('club')] = 'club';
data['itemType'][data['itemName'].str.contains('blade')] = 'sword';
data['itemType'][data['itemName'].str.contains('knife')] = 'knife';

data['itemType'][data['itemName'].str.contains('dbs')] = 'dbs';
data['itemType'][data['itemName'].str.contains('pump')] = 'pump';
data['itemType'][data['itemName'].str.contains('python')] = 'python';
data['itemType'][data['itemName'].str.contains('mp5')] = 'mp5';
data['itemType'][data['itemName'].str.contains('sar')] = 'sar';
data['itemType'][data['itemName'].str.contains('revolver')] = 'revolver';
data['itemType'][data['itemName'].str.contains('smg')] = 'smg';
data['itemType'][data['itemName'].str.contains('ak47')] = 'ak47';
data['itemType'][data['itemName'].str.contains('sap')] = 'sap';
data['itemType'][data['itemName'].str.contains('smg')] = 'smg';
data['itemType'][data['itemName'].str.contains('bolt')] = 'bar';
data['itemType'][data['itemName'].str.contains('47')] = 'ak47';
data['itemType'][data['itemName'].str.contains('bar')] = 'bar';
data['itemType'][data['itemName'].str.contains('300')] = 'lr300';
data['itemType'][data['itemName'].str.contains('eoka')] = 'eoka';
data['itemType'][data['itemName'].str.contains('pipe')] = 'waterpipe';
data['itemType'][data['itemName'].str.contains(' ak')] = 'ak47';
data['itemType'][data['itemName'].str.contains('ak ')] = 'ak47';

data['itemType'][data['itemName'].str.contains('grenade')] = 'grenade';
data['itemType'][data['itemName'].str.contains('satchel')] = 'satchel';
data['itemType'][data['itemName'].str.contains('rocket')] = 'launcher';
data['itemType'][data['itemName'].str.contains('launcher')] = 'launcher';

data['itemType'][data['itemName'].str.contains('crossbow')] = 'crossbow';

data['itemType'][data['itemName'].str.contains('hoodie')] = 'hoodie';
data['itemType'][data['itemName'].str.contains('bandana')] = 'bandana';
data['itemType'][data['itemName'].str.contains('boonie')] = 'boonie';
data['itemType'][data['itemName'].str.contains('cap')] = 'cap';
data['itemType'][data['itemName'].str.contains('shoes')] = 'hide boots';
data['itemType'][data['itemName'].str.contains('jacket')] = 'jacket';
data['itemType'][data['itemName'].str.contains('balaclava')] = 'balaclava';
data['itemType'][data['itemName'].str.contains('beenie')] = 'beenie';
data['itemType'][data['itemName'].str.contains('headwrap')] = 'headwrap';
data['itemType'][data['itemName'].str.contains('pants')] = 'pants';
data['itemType'][data['itemName'].str.contains('boots')] = 'boots';
data['itemType'][data['itemName'].str.contains('shirt')] = 'tshirt';
data['itemType'][data['itemName'].str.contains('gloves')] = 'leather gloves';
data['itemType'][data['itemName'].str.contains('short')] = 'shorts';

data['itemType'][data['itemName'].str.contains('poncho')] = 'poncho';
data['itemType'][data['itemName'].str.contains('mask')] = 'metal face mask';
data['itemType'][data['itemName'].str.contains('kilt')] = 'rs kilt';
data['itemType'][data['itemName'].str.contains('bucket')] = 'bucket';
data['itemType'][data['itemName'].str.contains('chest plate')] = 'metal chest plate';
data['itemType'][data['itemName'].str.contains('sign vest')] = 'rs jacket';
data['itemType'][data['itemName'].str.contains('sign pants')] = 'rs kilt';
data['itemType'][data['itemName'].str.contains('sign jacket')] = 'rs jacket';
data['itemType'][data['itemName'].str.contains('sign kilt')] = 'rs kilt';
data['itemType'][data['itemName'].str.contains('vest')] = 'rs jacket';

data['itemType'][data['itemType'].str.contains('beenie')] = 'beanie';

##############
# Graphs for blog post

# Store vs Market
test = data;
index = range(0, data.shape[0] * 2 + 1);
columns = ['cat', 'price'];
holder = pd.DataFrame(index=index, columns=columns)
holder['cat'][0:data.shape[0]] = "OG_price_NZ";
holder['price'][0:data.shape[0]] = data["OG_price_NZ"];
holder['cat'][data.shape[0]:data.shape[0] * 2] = "priceAvg";
holder['price'][data.shape[0]:data.shape[0] * 2] = data["priceAvg"];

f, ax = plt.subplots(figsize=(7, 5))
for index, row in test.iterrows():
    # ax = sns.pointplot(x="cat", y="price", data=test[row])
    plt.plot([0, 1], [row['OG_price_NZ'], row['priceAvg']], 'ko-', alpha=0.05)
sns.pointplot(x="cat", y="price", data=holder, estimator=np.median, capsize=.1, color="#cf432c")
ax.set_xlim(-0.5, 1.5);
ax.set_ylim(0, 10);
plt.ylabel('NZD $');
plt.xlabel('Prices');
plt.title('Change in price from Store to Market')
ax.set_xticks([-0.5, 0, 1, 1.5]);
ax.set_xticklabels(["", "Original", "Average"]);
fmt = '${x:,.0f}'
tick = tkr.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

sci.wilcoxon(data['OG_price_NZ'], data['priceAvg'])

f, ax = plt.subplots(figsize=(7, 5))
sns.kdeplot(data['OG_price_NZ'], shade=True, color="k", bw=1)
sns.kdeplot(data['priceAvg'], shade=True, color="#cf432c", bw=1, clip=[0, 50])
ax.set_xlim(0, 10);
plt.title('Store prices vs Market prices')
fmt = '${x:,.0f}'
tick = tkr.StrMethodFormatter(fmt)
ax.xaxis.set_major_formatter(tick)
plt.ylabel('KDE');
plt.xlabel('NZD $');
plt.legend(['Store', 'Market']);
plt.text(7, 0.25, 'Avg change: $' + str(round(data['OG_to_avg'].mean(), 2)), fontsize=12);
plt.text(7, 0.23, 'Med change: $' + str(round(data['OG_to_avg'].median(), 2)), fontsize=12);

# Initial
# Initial dist
f, ax = plt.subplots(1)
ax.hist(data['initial'], bins=800, color="#cf432c");
plt.xlim(-20, 20)
ax.axvline(x=0, ymin=0, ymax=175, linewidth=0.5, color='k')
plt.ylabel('# of Items')
plt.xlabel('Initial price change')
plt.text(10, 575, 'Avg: $' + str(round(data['initial'].mean(), 2)), fontsize=12);
plt.text(10, 545, 'Med: $' + str(round(data['initial'].median(), 2)), fontsize=12);
plt.title('Day 1 to Day 2 price change')
fmt = '${x:,.0f}'
tick = tkr.StrMethodFormatter(fmt)
ax.xaxis.set_major_formatter(tick)

# Max
f, ax = plt.subplots(1)
ax.hist(data['maxIdx'], bins=100, color="#cf432c");
plt.xlim(-0, 800)
plt.ylabel('# of Items')
plt.xlabel('Day of max price')
plt.text(600, 445, 'Avg max: ' + str(int(round(data['maxIdx'].mean(), 0))), fontsize=12);
plt.text(600, 420, 'Med max: ' + str(int(round(data['maxIdx'].median(), 0))), fontsize=12);
plt.text(600, 395, 'Mode max: ' + str(int(round(data['maxIdx'].mode()[0], 2))), fontsize=12);
plt.title('Distribution of max price days')

(data['maxIdx'] < 2).sum()

(data['maxIdx'] == 0).sum()
(data['maxIdx'] == 1).sum()
(data['maxIdx'] == 2).sum()

# Min
f, ax = plt.subplots(1)
ax.hist(data['minIdx'], bins=100, color="#cf432c");
plt.xlim(-0, 800)
plt.ylabel('# of Items')
plt.xlabel('Day of min price')
plt.text(600, 300, 'Avg max: ' + str(int(round(data['minIdx'].mean(), 0))), fontsize=12);
plt.text(600, 285, 'Med max: ' + str(int(round(data['minIdx'].median(), 0))), fontsize=12);
plt.text(600, 270, 'Mode max: ' + str(int(round(data['minIdx'].mode()[0], 2))), fontsize=12);
plt.title('Distribution of min price days')

# smooth/appreciation

a = data[data['smoothChange'].notnull()];

f, ax = plt.subplots(1)
ax.hist(a['smoothChange'], bins=1000, color="#cf432c");
plt.xlabel('Change in Price')
plt.ylabel('# of items')
plt.axvline(x=0, ymin=0, ymax=175, linewidth=0.5, color='k')
ax.set_xlim(-50, 50)
formatter = tkr.FormatStrFormatter('$%1.2f')
ax.xaxis.set_major_formatter(formatter)
plt.text(30, 265, 'Avg: $' + str(round(a['smoothChange'].mean(), 2)), fontsize=12);
plt.text(30, 252, 'Med: $' + str(round(a['smoothChange'].median(), 2)), fontsize=12);

sci.wilcoxon(data['OG_to_avg'], data['smoothChange'])

## swing

f, ax = plt.subplots(1)
ax.hist(data['swing'], bins=2000, color="#cf432c");
plt.xlim(0, 50)
plt.ylabel('# of Items')
plt.xlabel('Swing in price $')
plt.text(39, 84, 'Avg: $' + str(round(data['swing'].mean(), 2)), fontsize=12);
plt.text(39, 79, 'Med: $' + str(round(data['swing'].median(), 2)), fontsize=12);
plt.title('Distribution of price swings')
formatter = tkr.FormatStrFormatter('$%1.2f')
ax.xaxis.set_major_formatter(formatter)

## maxMinIdxDiff
f, ax = plt.subplots(1)
ax.hist(data['maxMinIdxDiff'], bins=300, color="#cf432c");
plt.xlim(-800, 800)
plt.ylabel('# of Items')
plt.xlabel('Swing duration (days)')
plt.text(515, 40, 'Avg: ' + str(int(round(data['maxMinIdxDiff'].mean(), 0))), fontsize=12);
plt.text(515, 38, 'Med: ' + str(int(round(data['maxMinIdxDiff'].median(), 0))), fontsize=12);
plt.text(515, 36, 'Mode: ' + str(int(round(data['maxMinIdxDiff'].mode()[0], 2))), fontsize=12);
plt.title('Distribution of swing durations')

sci.normaltest(data['maxMinIdxDiff'])
sci.skew(data['maxMinIdxDiff'])
sci.skewtest(data['maxMinIdxDiff'])

## Index fund
# marketDelta
# marketPrice
# marketVol

deltaVector = marketDelta.mean(axis=1, skipna=True);
priceVector = marketPrice.mean(axis=1, skipna=True);
priceCount = marketPrice.count(axis=1)
volVector = marketVol.mean(axis=1, skipna=True);
volCount = marketVol.count(axis=1)

goodDates = volCount > 0;

deltaVector = deltaVector[goodDates];
priceVector = priceVector[goodDates];
priceCount = priceCount[goodDates];
volVector = volVector[goodDates];
volCount = volCount[goodDates];

priceVolNorm = priceVector / priceCount;
volItemNorm = volVector * volCount;
priceRoll = priceVector.rolling('5d').mean();

years = mdates.YearLocator()  # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')

f, ax = plt.subplots(figsize=(12, 5))
plt.plot(volItemNorm, color="#cf432c")
plt.ylabel('Index volume')
plt.xlabel('Date')
plt.title('COBALT Index Fund')
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)
ax.axvline(x='2015-12-25', ymin=0, ymax=10, linewidth=0.5, color='r', alpha=0.5)
ax.axvline(x='2016-12-25', ymin=0, ymax=10, linewidth=0.5, color='r', alpha=0.5)
ax.axvline(x='2017-12-25', ymin=0, ymax=10, linewidth=0.5, color='r', alpha=0.5)
ax.axvline(x='2018-12-25', ymin=0, ymax=10, linewidth=0.5, color='r', alpha=0.5)
ax.axvline(x='2016-06-20', ymin=0, ymax=10, linewidth=0.5, color='k', alpha=0.5)
ax.axvline(x='2017-06-20', ymin=0, ymax=10, linewidth=0.5, color='k', alpha=0.5)
ax.axvline(x='2018-06-20', ymin=0, ymax=10, linewidth=0.5, color='k', alpha=0.5)
plt.xlim('2015-07-16', '2019-03-31')

f, ax = plt.subplots(1, 1, figsize=(12, 5))
plt.plot(priceVector, color="#cf432c")
plt.ylabel('Index ($)')
plt.xlabel('Date')
plt.title('COBALT Index Fund')
fmt = '${x:,.0f}'
tick = tkr.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)
ax.axvline(x='2015-12-25', ymin=0, ymax=10, linewidth=0.5, color='r', alpha=0.5)
ax.axvline(x='2016-12-25', ymin=0, ymax=10, linewidth=0.5, color='r', alpha=0.5)
ax.axvline(x='2017-12-25', ymin=0, ymax=10, linewidth=0.5, color='r', alpha=0.5)
ax.axvline(x='2018-12-25', ymin=0, ymax=10, linewidth=0.5, color='r', alpha=0.5)
ax.axvline(x='2016-06-20', ymin=0, ymax=10, linewidth=0.5, color='k', alpha=0.5)
ax.axvline(x='2017-06-20', ymin=0, ymax=10, linewidth=0.5, color='k', alpha=0.5)
ax.axvline(x='2018-06-20', ymin=0, ymax=10, linewidth=0.5, color='k', alpha=0.5)
plt.xlim('2015-07-16', '2019-03-31')

f, ax = plt.subplots(1, 2, figsize=(12, 5))
plt.bar(pd.date_range('2015-07-16', '2019-03-31'), volItemNorm, align='edge', color="#cf432c", edgecolor="#cf432c")
plt.ylabel('Index volume')
plt.xlabel('Date')
plt.title('COBALT Index Fund')

# THE plot
f, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 5), gridspec_kw={'height_ratios': [4, 1], 'wspace': 0.0, 'hspace': 0.0})
ax1.plot(priceVector, color="#cf432c", alpha=0.5)
ax1.plot(priceRoll, color="#cf432c")
ax1.tick_params(
    axis='x',  # changes apply to the x-axis
    which='both',  # both major and minor ticks are affected
    bottom=False,  # ticks along the bottom edge are off
    top=False,  # ticks along the top edge are off
    labelbottom=False)  # labels along the bottom edge are off

ax1.set_ylabel('Index ($)')
ax1.set_ylim(0, 9)
ax1.set_yticks([0, 3, 6, 9]);

ax1.set_title('COBALT Index Fund')
fmt = '${x:,.0f}'
tick = tkr.StrMethodFormatter(fmt)
ax1.yaxis.set_major_formatter(tick)

ax1.axvline(x='2015-12-25', ymin=0, ymax=10, linewidth=0.5, color='r', alpha=0.5)
ax1.axvline(x='2016-12-25', ymin=0, ymax=10, linewidth=0.5, color='r', alpha=0.5)
ax1.axvline(x='2017-12-25', ymin=0, ymax=10, linewidth=0.5, color='r', alpha=0.5)
ax1.axvline(x='2018-12-25', ymin=0, ymax=10, linewidth=0.5, color='r', alpha=0.5)
ax1.axvline(x='2016-06-20', ymin=0, ymax=10, linewidth=0.5, color='k', alpha=0.5)
ax1.axvline(x='2017-06-20', ymin=0, ymax=10, linewidth=0.5, color='k', alpha=0.5)
ax1.axvline(x='2018-06-20', ymin=0, ymax=10, linewidth=0.5, color='k', alpha=0.5)
ax1.set_xlim('2015-07-16', '2019-03-31')

ax2.bar(pd.date_range('2015-07-16', '2019-03-31'), volItemNorm, align='edge', color="#222423", edgecolor="#222423")
ax2.set_ylabel('Index volume')
ax2.set_xlabel('Date')
ax2.set_xlim('2015-07-16', '2019-03-31')

ax2.xaxis.set_major_locator(years)
ax2.xaxis.set_major_formatter(yearsFmt)
ax2.xaxis.set_minor_locator(months)
ax2.set_yticks([0, 15000, 30000]);
ax2.set_yticklabels(['0', '15k', '30k']);

plt.bar(pd.date_range('2015-07-16', '2019-03-31'), volItemNorm, align='edge', color="#222423", edgecolor="#222423")

# summer june 20

s = pd.date_range('2017-01-01', '2019-03-31', freq='D').to_series();
daysWeek = s.dt.dayofweek;

volItemNormNew = volItemNorm[s];
priceVectorNew = priceVector[s];

# plt.scatter(daysWeek,volItemNormNew,color ="#cf432c",alpha=0.5);
# mon = np.mean(volItemNormNew[daysWeek == 0])

f, ax = plt.subplots(figsize=(7, 5))
sns.violinplot(x=daysWeek, y=volItemNormNew)
plt.ylabel('Volume of trades')
plt.xlabel('Day of the week')
plt.title('Trading volume by day')

sci.f_oneway(volItemNormNew[daysWeek == 0], volItemNormNew[daysWeek == 1], volItemNormNew[daysWeek == 2],
             volItemNormNew[daysWeek == 3], volItemNormNew[daysWeek == 4], volItemNormNew[daysWeek == 5],
             volItemNormNew[daysWeek == 6])
print(pairwise_tukeyhsd(volItemNormNew, daysWeek))

f, ax = plt.subplots(figsize=(7, 5))
sns.violinplot(x=daysWeek, y=priceVectorNew)
plt.ylabel('Price of Index')
plt.xlabel('Day of the week')
plt.title('Prices by day')
fmt = '${x:,.0f}'
tick = tkr.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

sci.f_oneway(priceVectorNew[daysWeek == 0], priceVectorNew[daysWeek == 1], priceVectorNew[daysWeek == 2],
             priceVectorNew[daysWeek == 3], priceVectorNew[daysWeek == 4], priceVectorNew[daysWeek == 5],
             priceVectorNew[daysWeek == 6])
print(pairwise_tukeyhsd(priceVectorNew, daysWeek))

f, ax = plt.subplots(figsize=(12, 5))
plt.plot(priceVolNorm, color="#cf432c")
plt.ylabel('Price change ($)')
plt.xlabel('Date')

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)

# groups

# tiers
dataT = data[data['tier'].notnull()];

f, ax = plt.subplots(figsize=(7, 5))
g = sns.boxplot(x='tier', y='priceAvg', data=dataT)
ax.set_ylim(0, 15)
plt.ylabel('Avg Price')
plt.xlabel('Tier')
plt.title('Avg prices by tier')
fmt = '${x:,.0f}'
tick = tkr.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

sci.f_oneway(dataT['priceAvg'][dataT['tier'] == 0], dataT['priceAvg'][dataT['tier'] == 1],
             dataT['priceAvg'][dataT['tier'] == 2], dataT['priceAvg'][dataT['tier'] == 3],
             dataT['priceAvg'][dataT['tier'] == 4])
print(pairwise_tukeyhsd(dataT['priceAvg'], dataT['tier']))

# armor
dataArmor = data[data['itemTypeGeneral'] == 'armor'];
dataArmor = dataArmor[dataArmor['itemType'] != ''];
dataArmor['itemType'][dataArmor['itemType'].str.contains('bone helmet')] = 'bone';
dataArmor['itemType'][dataArmor['itemType'].str.contains('metal chest plate')] = 'MCP';
dataArmor['itemType'][dataArmor['itemType'].str.contains('metal face mask')] = 'MFM';
dataArmor['itemType'][dataArmor['itemType'].str.contains('rs jacket')] = 'RSJ';
dataArmor['itemType'][dataArmor['itemType'].str.contains('rs kilt')] = 'RSK';

(dataArmor['itemType'] == 'bone').sum()
(dataArmor['itemType'] == 'poncho').sum()

(dataArmor['itemType'] == 'RSJ').sum()
(dataArmor['itemType'] == 'MCP').sum()

sci.f_oneway(dataArmor['priceAvg'][dataArmor['itemType'] == 'RSJ'],
             dataArmor['priceAvg'][dataArmor['itemType'] == 'RSK'],
             dataArmor['priceAvg'][dataArmor['itemType'] == 'MFM'],
             dataArmor['priceAvg'][dataArmor['itemType'] == 'MCP'],
             dataArmor['priceAvg'][dataArmor['itemType'] == 'coffee'])

sci.f_oneway(dataArmor['swing'][dataArmor['itemType'] == 'RSJ'], dataArmor['swing'][dataArmor['itemType'] == 'RSK'],
             dataArmor['swing'][dataArmor['itemType'] == 'MFM'], dataArmor['swing'][dataArmor['itemType'] == 'MCP'],
             dataArmor['swing'][dataArmor['itemType'] == 'coffee'])
sci.f_oneway(dataArmor['OGNZAvgDiff'][dataArmor['itemType'] == 'RSJ'],
             dataArmor['OGNZAvgDiff'][dataArmor['itemType'] == 'RSK'],
             dataArmor['OGNZAvgDiff'][dataArmor['itemType'] == 'MFM'],
             dataArmor['OGNZAvgDiff'][dataArmor['itemType'] == 'MCP'],
             dataArmor['OGNZAvgDiff'][dataArmor['itemType'] == 'coffee'])

f, ax = plt.subplots(figsize=(7, 5))
sns.boxplot(x='itemType', y='priceAvg', data=dataArmor)
ax.set_ylim(0, 25)
plt.ylabel('Avg Price')
plt.xlabel('')
plt.title('Avg prices by armor type')
fmt = '${x:,.0f}'
tick = tkr.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

a = dataArmor.describe();

# guns
dataGuns = data[data['itemTypeGeneral'] == 'gun'];
dataGuns['itemType'][dataGuns['itemType'].str.contains('crossbow')] = 'crossy';
dataGuns['itemType'][dataGuns['itemType'].str.contains('revolver')] = 'rev';
dataGuns['itemType'][dataGuns['itemType'].str.contains('waterpipe')] = 'wp';
dataGuns['itemType'][dataGuns['itemType'].str.contains('thompson')] = 'tomy';

f, ax = plt.subplots(figsize=(7, 5))
sns.boxplot(x='itemType', y='priceAvg', data=dataGuns)
ax.set_ylim(0, 50)
plt.ylabel('Avg Price')
plt.xlabel('')
plt.title('Avg prices by gun type')
fmt = '${x:,.0f}'
tick = tkr.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

sci.f_oneway(dataGuns['priceAvg'][dataGuns['itemType'] == 'eoka'],
             dataGuns['priceAvg'][dataGuns['itemType'] == 'crossy'],
             dataGuns['priceAvg'][dataGuns['itemType'] == 'dbs'], dataGuns['priceAvg'][dataGuns['itemType'] == 'rev'],
             dataGuns['priceAvg'][dataGuns['itemType'] == 'wp'], dataGuns['priceAvg'][dataGuns['itemType'] == 'pump'],
             dataGuns['priceAvg'][dataGuns['itemType'] == 'python'],
             dataGuns['priceAvg'][dataGuns['itemType'] == 'sap'], dataGuns['priceAvg'][dataGuns['itemType'] == 'sar'],
             dataGuns['priceAvg'][dataGuns['itemType'] == 'smg'], dataGuns['priceAvg'][dataGuns['itemType'] == 'tomy'],
             dataGuns['priceAvg'][dataGuns['itemType'] == 'ak47'], dataGuns['priceAvg'][dataGuns['itemType'] == 'bar'],
             dataGuns['priceAvg'][dataGuns['itemType'] == 'mp5'], dataGuns['priceAvg'][dataGuns['itemType'] == 'lr300'])
sci.f_oneway(dataGuns['OGNZAvgDiff'][dataGuns['itemType'] == 'eoka'],
             dataGuns['OGNZAvgDiff'][dataGuns['itemType'] == 'crossy'],
             dataGuns['OGNZAvgDiff'][dataGuns['itemType'] == 'dbs'],
             dataGuns['OGNZAvgDiff'][dataGuns['itemType'] == 'rev'],
             dataGuns['OGNZAvgDiff'][dataGuns['itemType'] == 'wp'],
             dataGuns['OGNZAvgDiff'][dataGuns['itemType'] == 'pump'],
             dataGuns['OGNZAvgDiff'][dataGuns['itemType'] == 'python'],
             dataGuns['OGNZAvgDiff'][dataGuns['itemType'] == 'sap'],
             dataGuns['OGNZAvgDiff'][dataGuns['itemType'] == 'sar'],
             dataGuns['OGNZAvgDiff'][dataGuns['itemType'] == 'smg'],
             dataGuns['OGNZAvgDiff'][dataGuns['itemType'] == 'tomy'],
             dataGuns['OGNZAvgDiff'][dataGuns['itemType'] == 'ak47'],
             dataGuns['OGNZAvgDiff'][dataGuns['itemType'] == 'bar'],
             dataGuns['OGNZAvgDiff'][dataGuns['itemType'] == 'mp5'],
             dataGuns['OGNZAvgDiff'][dataGuns['itemType'] == 'lr300'])
sci.f_oneway(dataGuns['swing'][dataGuns['itemType'] == 'eoka'], dataGuns['swing'][dataGuns['itemType'] == 'crossy'],
             dataGuns['swing'][dataGuns['itemType'] == 'dbs'], dataGuns['swing'][dataGuns['itemType'] == 'rev'],
             dataGuns['swing'][dataGuns['itemType'] == 'wp'], dataGuns['swing'][dataGuns['itemType'] == 'pump'],
             dataGuns['swing'][dataGuns['itemType'] == 'python'], dataGuns['swing'][dataGuns['itemType'] == 'sap'],
             dataGuns['swing'][dataGuns['itemType'] == 'sar'], dataGuns['swing'][dataGuns['itemType'] == 'smg'],
             dataGuns['swing'][dataGuns['itemType'] == 'tomy'], dataGuns['swing'][dataGuns['itemType'] == 'ak47'],
             dataGuns['swing'][dataGuns['itemType'] == 'bar'], dataGuns['swing'][dataGuns['itemType'] == 'mp5'],
             dataGuns['swing'][dataGuns['itemType'] == 'lr300'])

print(pairwise_tukeyhsd(dataGuns['priceAvg'], dataGuns['itemType']))

a = dataGuns.describe();

# RP
dataRP = data[data['itemTypeGeneral'] == 'RP'];
dataRP = dataRP[dataRP['itemType'] != 'building'];
dataRP = dataRP[dataRP['itemType'] != 'decoration'];
dataRP = dataRP[dataRP['itemType'] != 'table'];
dataRP = dataRP[dataRP['itemType'] != 'water purifier'];
dataRP = dataRP[dataRP['itemType'] != 'target'];
dataRP = dataRP[dataRP['itemType'] != 'lantern'];
dataRP = dataRP[dataRP['itemType'] != 'fireplace'];

dataRP['itemType'][dataRP['itemType'].str.contains('sheet metal door')] = 'sm door';
dataRP['itemType'][dataRP['itemType'].str.contains('sleeping bag')] = 'bag';
dataRP['itemType'][dataRP['itemType'].str.contains('wooden door')] = 'w door';
dataRP['itemType'][dataRP['itemType'].str.contains('wood door')] = 'w door';
dataRP['itemType'][dataRP['itemType'].str.contains('garage')] = 'g';
dataRP['itemType'][dataRP['itemType'].str.contains('garage door')] = 'g';

f, ax = plt.subplots(figsize=(7, 5))
sns.boxplot(x='itemType', y='priceAvg', data=dataRP)
ax.set_ylim(0, 20)
plt.ylabel('Avg Price')
plt.xlabel('')
plt.title('Avg prices by role playing type')
fmt = '${x:,.0f}'
tick = tkr.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

a = dataRP.describe();

# clothing
dataCloth = data[data['itemTypeGeneral'] == 'clothing'];
dataCloth = dataCloth[dataCloth['itemType'] != 'beanie'];
dataCloth = dataCloth[dataCloth['itemType'] != 'burlap shoes'];
dataCloth = dataCloth[dataCloth['itemType'] != 'burlap gloves'];
dataCloth = dataCloth[dataCloth['itemType'] != 'burlap shows'];
dataCloth = dataCloth[dataCloth['itemType'] != 'crop top'];
dataCloth = dataCloth[dataCloth['itemType'] != 'hide boots'];
dataCloth = dataCloth[dataCloth['itemType'] != 'hide halterneck'];
dataCloth = dataCloth[dataCloth['itemType'] != 'hide poncho'];
dataCloth = dataCloth[dataCloth['itemType'] != 'leather boots'];
dataCloth = dataCloth[~dataCloth['itemType'].str.contains('miner')];
dataCloth = dataCloth[dataCloth['itemType'] != 'rs jacket'];
dataCloth = dataCloth[dataCloth['itemType'] != 'rs kilt'];
dataCloth = dataCloth[dataCloth['itemType'] != 'shorts'];
dataCloth = dataCloth[dataCloth['itemType'] != 'snow jacket'];
dataCloth = dataCloth[dataCloth['itemType'] != 'skirt'];

dataCloth['itemType'][dataCloth['itemType'].str.contains('sheet metal door')] = 'sm door';

f, ax = plt.subplots(figsize=(7, 5))
sns.boxplot(x='itemType', y='OGNZAvgDiff', data=dataCloth)
ax.set_ylim(0, 15)
plt.ylabel('Avg Price')
plt.xlabel('')
plt.title('Avg prices by clothing')
fmt = '${x:,.0f}'
tick = tkr.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

a = dataCloth.describe();

# make sure you sort by priceAvg (or whatever) first
# top
dataTop = data.head(50);
a = dataTop.describe();

dataTop['itemTypeGeneral'].str.contains('clothing').sum()
dataTop['itemTypeGeneral'].str.contains('armor').sum()

dataTop['itemTypeGeneral'].str.contains('gun').sum()
dataTop['itemTypeGeneral'].str.contains('RP').sum()

# bot
dataBot = data.tail(100);
dataBot = dataBot[dataBot['itemType'] != 'decoration'];
dataBot = dataBot[dataBot['itemType'] != 'building'];
dataBot = dataBot[dataBot['itemType'] != 'crafting'];
dataBot = dataBot[dataBot['itemType'] != 'loot'];

b = dataBot.describe();

dataBot['itemTypeGeneral'].str.contains('clothing').sum()
dataBot['itemTypeGeneral'].str.contains('armor').sum()

# tests
sci.mannwhitneyu(dataTop['tier'], dataBot['tier'])
sci.mannwhitneyu(dataTop['timeOnMarket'], dataBot['timeOnMarket'])
sci.mannwhitneyu(dataTop['OGNZAvgDiff'], dataBot['OGNZAvgDiff'])

# gold

golden = data.index.tolist();
golden = pd.Series(golden)
goldenIdx = golden.str.contains('gold');

goldenMoney = pd.Series(data['OGNZAvgDiff'])
goldenMoney = goldenMoney.reset_index();

dataGold = goldenMoney[goldenIdx];

b = dataGold.describe();

sci.mannwhitneyu(dataGold['OGNZAvgDiff'], data['OGNZAvgDiff'])

#############
# Rainn test
f, ax = plt.subplots(figsize=(7, 5))
dy = "tier";
dx = "OGNZAvgDiff";
ort = "h";
pal = sns.color_palette(n_colors=1)

pal = "Set2"
f, ax = plt.subplots(figsize=(7, 5))
ax = pt.half_violinplot(x=dx, y=dy, data=data, palette=pal, bw=0.2, cut=0,
                        scale="area", width=.6, inner=None, orient=ort)
ax = sns.stripplot(x=dx, y=dy, data=data, palette=pal, edgecolor="white",
                   size=3, jitter=1, zorder=0, orient=ort)
ax = sns.boxplot(x=dx, y=dy, data=data, color="black", width=.15, zorder=10, \
                 showcaps=True, boxprops={'facecolor': 'none', "zorder": 10}, \
                 showfliers=True, whiskerprops={'linewidth': 2, "zorder": 10}, \
                 saturation=1, orient=ort)
ax.set_xlim(0, 50);

dy = "tier";
dx = "priceAvg";
ort = "h";
pal = "Set2";
sigma = .2;

ax = pt.RainCloud(x=dx, y=dy, data=data, palette=pal, bw=sigma,
                  width_viol=.6, figsize=(7, 5), orient=ort)
ax.set_xlim(0, 50)

############


# clean up data
data = data[data['priceIncrease'] > -100]
data = data[data['priceAvg'] > 0.5]  # get rid of random drop skins

# make my plots pretty
sns.set_palette("Blues_r");

# for graphs
labels = ['tier', 'itemTypeGeneral', 'itemType', 'OG_price', 'OG_price_NZ', 'initial', 'timeOnMarket', 'priceAvg',
          'priceSD', 'priceIncrease', 'smoothChange', 'maxPrice', 'maxIdx', 'minPrice', 'minIdx', 'maxMinIdxDiff',
          'swing', 'volAvg', 'volSD', 'slope', 'rr', 'OGNZAvgDiff'];

# handy descriptive stats from Pandas
dataDesc = data.describe();
sns.pairplot(data)

data.median()
data.sem()

forCorr = data.loc[:,
          ['priceAvg', 'OG_price_NZ', 'initial', 'priceIncrease', 'smoothChange', 'maxPrice', 'maxIdx', 'minIdx',
           'maxMinIdxDiff', 'swing', 'volAvg']];
corrLabels = ['priceAvg', 'OG_price_NZ', 'initial', 'priceIncrease', 'smoothChange', 'maxPrice', 'maxIdx', 'minIdx',
              'maxMinIdxDiff', 'swing', 'volAvg'];

# Correlation to see how data is related
correlations = forCorr.corr()

f, ax = plt.subplots(1)
f.set_size_inches(4, 3)
plt.set_cmap('RdYlBu_r')
cax = ax.matshow(correlations, vmin=-1, vmax=1)
cb = f.colorbar(cax)
cb.ax.set_yticklabels(cb.ax.get_yticklabels(), fontsize=13)
ticks = np.arange(0, len(corrLabels), 1)
ax.set_xticks(ticks[0:len(correlations)])
ax.set_yticks(ticks[0:len(correlations)])
ticks = correlations.index.tolist()  # label axes from corr index which is labels
ax.set_xticklabels(ticks[0:len(correlations)])
ax.set_yticklabels(ticks[0:len(correlations)])
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xticks(rotation=-90)
# plt.title('Correlations', fontsize=32)
# Minor ticks
ax.set_xticks(np.arange(-.5, len(correlations) - 1, 1), minor=True);
ax.set_yticks(np.arange(-.5, len(correlations) - 1, 1), minor=True);
# Gridlines based on minor ticks
ax.grid(which='minor', color='k', linestyle='-', linewidth=2)
plt.savefig(gameID + 'Corr.png', bbox_inches='tight')

plt.figure()
g = sns.distplot(data['timeOnMarket'], bins=100, kde=False)
ax = g.axes
ax.set_xlim(0, data["timeOnMarket"].max())
plt.ylabel('# of Skins')
plt.xlabel('Time on Market (days)')
plt.savefig(gameID + 'timeMarketDist.png', bbox_inches='tight')

a = data[data['smoothChange'].notnull()];

f, ax = plt.subplots(1)
ax.hist(a['smoothChange'], bins=1000);
plt.xlabel('Change in Price')
plt.ylabel('# of items')
plt.axvline(x=0, ymin=0, ymax=175, linewidth=0.5, color='k')
ax.set_xlim(-50, 50)
formatter = tkr.FormatStrFormatter('$%1.2f')
ax.xaxis.set_major_formatter(formatter)
plt.text(-48, 250, 'Avg change: $' + str(round(a['smoothChange'].mean(), 2)), fontsize=12);
plt.text(-48, 235, 'Med change: $' + str(round(a['smoothChange'].median(), 2)), fontsize=12);
plt.savefig(gameID + 'smoothChange.png', bbox_inches='tight')

f, ax = plt.subplots(1)
sns.distplot(a['smoothChange'], bins=1000, kde=False)
ax.set_xlim(-50, 50)
formatter = tkr.FormatStrFormatter('$%1.2f')
ax.xaxis.set_major_formatter(formatter)
plt.xlabel('Change in Price')
plt.ylabel('# of items')
plt.axvline(x=0, ymin=0, ymax=175, linewidth=0.5, color='k')
plt.text(-48, 250, 'Avg change: $' + str(round(a['smoothChange'].mean(), 2)), fontsize=12);
plt.text(-48, 235, 'Med change: $' + str(round(a['smoothChange'].median(), 2)), fontsize=12);
plt.savefig(gameID + 'smoothChange.png', bbox_inches='tight')

plt.figure()
g = sns.distplot(data['priceIncrease'], bins=1000, kde=False)
plt.xlim(-50, 50)
ax = g.axes
ax.axvline(x=0, ymin=0, ymax=175, linewidth=0.5)
plt.ylabel('# of Items')
plt.xlabel('Total price change')
plt.text(-48, 185, 'Avg change: $' + str(round(data['priceIncrease'].mean(), 2)), fontsize=12);
plt.text(-48, 165, 'Med change: $' + str(round(data['priceIncrease'].median(), 2)), fontsize=12);
# fmt = '${y:,.0f}'
# tick = tkr.StrMethodFormatter(fmt)
# ax.xaxis.set_major_formatter(tick)
plt.savefig(gameID + 'priceIncreaseDist.png', bbox_inches='tight')

f, ax = plt.subplots(1)
ax.scatter(x='timeOnMarket', y='priceIncrease', data=data, s=0.5, color='black', alpha=0.5)
m, b = np.polyfit(data['timeOnMarket'], data['priceIncrease'], 1)
ax.plot(data['priceIncrease'], m * data['priceIncrease'] + b, '-', color='black')
plt.title('Time vs Price Change')
plt.xlabel('timeOnMarket')
plt.ylabel('priceIncrease')
ax.set_ylim(0, 100)
fmt = '${x:,.0f}'
tick = tkr.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

f, ax = plt.subplots(1)
ax.scatter(x='timeOnMarket', y='priceAvg', data=data, s=0.5, color='black', alpha=0.5)
m, b = np.polyfit(data['timeOnMarket'], data['priceAvg'], 1)
ax.plot(data['timeOnMarket'], m * data['timeOnMarket'] + b, '-', color='black')
plt.title('Time vs Average Price')
plt.xlabel('timeOnMarket')
plt.ylabel('priceAvg')
ax.set_ylim(0, 20)
fmt = '${x:,.0f}'
tick = tkr.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

f, ax = plt.subplots(1)
ax.scatter(x='swing', y='priceAvg', data=data, s=0.5, color='black', alpha=0.5)
m, b = np.polyfit(data['swing'], data['priceAvg'], 1)
# ax.plot(data['swing'],m*data['swing']+b,'-',color='black')
plt.title('Swing vs Average Price')
plt.xlabel('priceAvg')
plt.ylabel('swing')
ax.set_ylim(0, 20)
ax.set_xlim(0, 30)
fmt = '${x:,.0f}'
tick = tkr.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

plt.figure()
g = sns.distplot(data['initial'], bins=800, kde=False)
plt.xlim(-20, 20)
ax = g.axes
ax.axvline(x=0, ymin=0, ymax=175, linewidth=0.5)
plt.ylabel('# of Items')
plt.xlabel('Initial price change')
plt.text(-19, 125, 'Avg change: $' + str(round(data['initial'].mean(), 2)), fontsize=12);
plt.text(-19, 115, 'Med change: $' + str(round(data['initial'].median(), 2)), fontsize=12);
plt.savefig(gameID + 'priceIncreaseDist.png', bbox_inches='tight')

plt.figure()
g = sns.distplot(data['maxIdx'], bins=100, kde=False)
ax = g.axes
plt.xlim(-0, 800)
# ax.axvline(x=0, ymin=0, ymax=200,linewidth=0.5)
plt.ylabel('# of Items')
plt.xlabel('Day of max price')
plt.text(600, 445, 'Avg max: ' + str(int(round(data['maxIdx'].mean(), 0))), fontsize=12);
plt.text(600, 420, 'Med max: ' + str(int(round(data['maxIdx'].median(), 0))), fontsize=12);
plt.text(600, 395, 'Mode max: ' + str(int(round(data['maxIdx'].mode()[0], 2))), fontsize=12);
plt.savefig(gameID + 'maxIdxDist.png', bbox_inches='tight')

plt.figure()
g = sns.distplot(data['minIdx'], bins=50, kde=False)
ax = g.axes
# plt.xlim(-100,100)
ax.axvline(x=0, ymin=0, ymax=200, linewidth=0.5)
ax.set_xlim(0, data["minIdx"].max())
plt.ylabel('# of Items')
plt.xlabel('Day of min price')
plt.text(720, 300, 'Avg min: ' + str(round(data['minIdx'].mean(), 2)), fontsize=12);
plt.text(720, 280, 'Med min: ' + str(round(data['minIdx'].median(), 2)), fontsize=12);
plt.text(720, 260, 'Mode min: ' + str(round(data['minIdx'].mode()[0], 2)), fontsize=12);
plt.savefig(gameID + 'minIdxDist.png', bbox_inches='tight')

plt.figure()
g = sns.distplot(data['maxMinIdxDiff'], bins=100, kde=False)
ax = g.axes
# plt.xlim(-100,100)
ax.axvline(x=0, ymin=0, ymax=200, linewidth=0.5)
plt.ylabel('# of Items')
plt.xlabel('Difference between max - min price day')
plt.text(-1150, 85, 'Avg diff: ' + str(round(data['maxMinIdxDiff'].mean(), 2)), fontsize=12);
plt.text(-1150, 79, 'Med diff: ' + str(round(data['maxMinIdxDiff'].median(), 2)), fontsize=12);
plt.savefig(gameID + 'maxMinIdxDiffDist.png', bbox_inches='tight')

plt.figure()
# g = sns.distplot(data['slope'],bins = 10000,kde=False,hist_kws=dict(cumulative=True))
g = sns.distplot(data['slope'], bins=20000, kde=False, hist_kws=dict(cumulative=False))
ax = g.axes
plt.xlim(-0.1, 0.1)
ax.axvline(x=0, ymin=0, ymax=200, linewidth=0.5)
plt.ylabel('# of Items')
plt.xlabel('Slope')
plt.text(-0.095, 110, 'Avg slope: ' + str(round(data['slope'].mean(), 2)), fontsize=12);
plt.text(-0.095, 100, 'Med slope: ' + str(round(data['slope'].median(), 2)), fontsize=12);
plt.savefig(gameID + 'slopeDist.png', bbox_inches='tight')

plt.figure()
g = sns.distplot(data['priceAvg'], bins=500, kde=False, hist_kws=dict(cumulative=False))
ax = g.axes
ax.axvline(x=0, ymin=0, ymax=200, linewidth=0.5)
ax.set_xlim(0, 30)
plt.ylabel('# of Items')
plt.xlabel('Average price')
plt.text(20, 110, 'Avg price: $' + str(round(data['priceAvg'].mean(), 2)), fontsize=12);
plt.text(20, 98, 'Med price: $' + str(round(data['priceAvg'].median(), 2)), fontsize=12);
plt.savefig(gameID + 'priceAvgDist.png', bbox_inches='tight')

plt.figure()
g = sns.distplot(data['OG_price_NZ'], bins=500, kde=False, hist_kws=dict(cumulative=False))
ax = g.axes
ax.axvline(x=0, ymin=0, ymax=200, linewidth=0.5)
ax.set_xlim(0, 30)
plt.ylabel('# of Items')
plt.xlabel('Original price')
plt.text(20, 110, 'Avg price: $' + str(round(data['OG_price_NZ'].mean(), 2)), fontsize=12);
plt.text(20, 98, 'Med price: $' + str(round(data['OG_price_NZ'].median(), 2)), fontsize=12);
plt.savefig(gameID + 'OGPriceDist.png', bbox_inches='tight')

plt.figure()
g = sns.distplot(data['maxPrice'], bins=1000, kde=False, hist_kws=dict(cumulative=False))
ax = g.axes
ax.axvline(x=0, ymin=0, ymax=200, linewidth=0.5)
ax.set_xlim(0, 100)
plt.ylabel('# of Items')
plt.xlabel('Average max price')
plt.text(67, 75, 'Avg max price: $' + str(round(data['maxPrice'].mean(), 2)), fontsize=12);
plt.text(67, 69, 'Med max price: $' + str(round(data['maxPrice'].median(), 2)), fontsize=12);
plt.savefig(gameID + 'maxPriceDist.png', bbox_inches='tight')

plt.figure()
g = sns.regplot(data['maxPrice'], data['minPrice'], data=data);
ax = g.axes
ax.set_ylim(0, data["minPrice"].max())
plt.savefig(gameID + 'maxMinScale.png', bbox_inches='tight')

plt.figure()
g = sns.regplot(data['OG_price_NZ'], data['minPrice'], data=data);
ax = g.axes
plt.savefig(gameID + 'maxMinAuto.png', bbox_inches='tight')

plt.figure()
g = sns.regplot(data['OG_price_NZ'], data['maxPrice'], data=data);
ax = g.axes

plt.figure()
g = sns.distplot(data['swing'], bins=1000, kde=False, hist_kws=dict(cumulative=False))
ax = g.axes
ax.axvline(x=0, ymin=0, ymax=200, linewidth=0.5)
ax.set_xlim(0, 100)
plt.ylabel('# of Items')
plt.xlabel('Swing in price')
plt.text(65, 90, 'Avg swing: $' + str(round(data['swing'].mean(), 2)), fontsize=12);
plt.text(65, 80, 'Med swing: $' + str(round(data['swing'].median(), 2)), fontsize=12);
plt.savefig(gameID + 'swingDist.png', bbox_inches='tight')

whatever = data['tier'][data['tier'] >= 0];

plt.figure()
g = sns.distplot(whatever, bins=4, kde=False, hist_kws=dict(cumulative=False))
ax = g.axes
ax.axvline(x=0, ymin=0, ymax=200, linewidth=0.5)
ax.set_xlim(0, 5)
plt.ylabel('# of Items')
plt.xlabel('Swing in price')
plt.text(70, 90, 'Avg swing: $' + str(round(data['swing'].mean(), 2)), fontsize=12);
plt.text(70, 85, 'Med swing: $' + str(round(data['swing'].median(), 2)), fontsize=12);

plt.figure()
g = sns.distplot(data['volAvg'], bins=2000, kde=False, hist_kws=dict(cumulative=False))
ax = g.axes
ax.axvline(x=0, ymin=0, ymax=200, linewidth=0.5)
ax.set_xlim(0, 50)
plt.ylabel('# of Items')
plt.xlabel('Avg volume')
plt.text(32, 75, 'Avg volume: ' + str(round(data['volAvg'].mean(), 2)), fontsize=12);
plt.text(32, 69, 'Med volume: ' + str(round(data['volAvg'].median(), 2)), fontsize=12);
plt.savefig(gameID + 'swingDist.png', bbox_inches='tight')

plt.figure()
g = sns.distplot(data['rr'], bins=100, kde=False, hist_kws=dict(cumulative=False))
ax = g.axes
ax.axvline(x=0, ymin=0, ymax=200, linewidth=0.5)
ax.set_xlim(0, 1)
plt.ylabel('# of Items')
plt.xlabel('R^2')
plt.text(0.60, 82, 'Avg R^2: ' + str(round(data['rr'].mean(), 2)), fontsize=12);
plt.text(0.60, 75, 'Med R^2: ' + str(round(data['rr'].median(), 2)), fontsize=12);
plt.savefig(gameID + 'rrDist.png', bbox_inches='tight')

plt.figure()
g = sns.violinplot(x='itemTypeGeneral', y='priceAvg', data=data)
ax = g.axes
ax.set_ylim(0, 50)

plt.figure()
g = sns.boxplot(x='itemTypeGeneral', y='priceAvg', data=data)
ax = g.axes
ax.set_ylim(0, 50)

plt.figure()
g = sns.boxplot(x='itemTypeGeneral', y='maxIdx', data=data)
ax = g.axes
ax.set_ylim(0, 1000)

plt.figure()
g = sns.boxplot(x='itemTypeGeneral', y='priceSD', data=data)
ax = g.axes
ax.set_ylim(0, 5)

plt.figure()
g = sns.boxplot(x='tier', y='priceAvg', data=data)
ax = g.axes
ax.set_ylim(0, 50)
ax.set_ylim(0, 15)

plt.figure()
g = sns.stripplot(x='tier', y='priceAvg', data=data)
ax = g.axes
ax.set_ylim(0, 20)

dataGuns = data[data['itemTypeGeneral'] == 'gun'];

plt.figure()
g = sns.boxplot(x='itemType', y='priceAvg', data=dataGuns)
ax = g.axes
ax.set_ylim(0, 50)

plt.figure()
g = sns.boxplot(x='itemType', y='swing', data=dataGuns)
ax = g.axes
ax.set_ylim(0, 50)

###
dataRP = data[data['itemTypeGeneral'] == 'RP'];

plt.figure()
g = sns.boxplot(x='itemType', y='priceAvg', data=dataRP)
ax = g.axes
ax.set_ylim(0, 30)

###
dataArmor = data[data['itemTypeGeneral'] == 'armor'];

plt.figure()
g = sns.boxplot(x='itemType', y='priceAvg', data=dataArmor)
ax = g.axes
ax.set_ylim(0, 50)

###
dataClothing = data[data['itemTypeGeneral'] == 'clothing'];

plt.figure()
g = sns.boxplot(x='itemType', y='priceAvg', data=dataClothing)
ax = g.axes
ax.set_ylim(0, 50)

###
dataTool = data[data['itemTypeGeneral'] == 'tool'];

plt.figure()
g = sns.boxplot(x='itemType', y='priceAvg', data=dataTool)
ax = g.axes
ax.set_ylim(0, 20)

###
dataExplosive = data[data['itemTypeGeneral'] == 'explosive'];

plt.figure()
g = sns.boxplot(x='itemType', y='priceAvg', data=dataExplosive)
ax = g.axes
ax.set_ylim(0, 20)

### maybe check like top 25 items or something
