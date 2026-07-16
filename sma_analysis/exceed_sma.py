#analyze the probability of the occurrence of spikes when the highest price exceeds the sma
from sma_calc import data
import pandas as pd
import matplotlib.pyplot as plt

data['exceed_sma'] = (
    (data['high'].shift(2) < data['SMA50']) # period can be modified to 10/20/50
    &
    (data['high'].shift(1) < data['SMA50'])
    &
    (data['high'] > data['SMA50'])
) # return whether the price exceeds the SMA50 the first time in a period of 3

data['drop_sma'] = (
    (data['high'].shift(2) > data['SMA50'])
    &
    (data['high'].shift(1) > data['SMA50'])
    &
    (data['high'] < data['SMA50'])
) # return whether the price drops below the SMA50 the first time in a period of 3

categories = []
values = []

table = pd.crosstab(data['spike_below'], data['exceed_sma'])
categories.append("Exceed SMA")
ratio = table.loc[True, True] / (table.loc[True, True] + table.loc[False, True])
values.append(ratio)
table = pd.crosstab(data['spike_below'], data['drop_sma'])
categories.append("Drop SMA")
ratio = table.loc[True, True] / (table.loc[True, True] + table.loc[False, True])
values.append(ratio)
categories.append("Average")
values.append(data['spike_above'].mean())
# plot the graph
bars = plt.bar(categories, values, color = 'skyblue', edgecolor = 'black')
plt.bar_label(bars, fmt='%.3f', padding=3)
plt.xlabel("Type")
plt.ylabel("Ratio of Upward Spikes")
plt.title("Ratio of Downward Spikes When Price Drops Below/Exceeds SMA50 at p = 3")
plt.show()