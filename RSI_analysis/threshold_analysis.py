from RSI_calc import data
import pandas as pd
import matplotlib.pyplot as plt

data['high_gain'] = data['high'] - data['open']
data['low_loss'] = data['open'] - data['low']

avg_gain_high = (data['gain'].shift(1).rolling(13).sum() + data['high_gain']) / 14
avg_loss_high = (data['loss'].shift(1).rolling(13).sum()) / 14
avg_gain_low = (data['gain'].shift(1).rolling(13).sum()) / 14
avg_loss_low = (data['loss'].shift(1).rolling(13).sum() + data['low_loss']) / 14

RS_high = avg_gain_high / avg_loss_high
RS_low = avg_gain_low / avg_loss_low
data['RSI_high'] = 100 - 100 / (1 + RS_high)
data['RSI_low'] = 100 - 100 / (1 + RS_low)
data['overbuying'] = (data['RSI_high'] > 70)
data['overbuying+'] = (data['RSI_high'] > 80)
data['overselling'] = (data['RSI_low'] < 30)
data['overselling+'] = (data['RSI_low'] < 20)

categories = []
values = []
table = pd.crosstab(data['overbuying'], data['spike_above'])
values.append(table.loc[True, True] / (table.loc[True, True] + table.loc[False, True]))
categories.append(" > 70") # ratio of upper spikes RSI > 70
table = pd.crosstab(data['overbuying+'], data['spike_above'])
values.append(table.loc[True, True] / (table.loc[True, True] + table.loc[False, True]))
categories.append("> 80") # ratio of upper spikes RSI > 80
values.append(data['spike_above'].mean())
categories.append("general_high") # average ratio of upper spikes

table = pd.crosstab(data['overselling'], data['spike_below'])
values.append(table.loc[True, True] / (table.loc[True, True] + table.loc[False, True]))
categories.append("< 30") # ratio of lower spikes RSI < 30
table = pd.crosstab(data['overselling+'], data['spike_below'])
values.append(table.loc[True, True] / (table.loc[True, True] + table.loc[False, True]))
categories.append("< 20") # ratio of upper spikes RSI < 20
values.append(data['spike_below'].mean())
categories.append("general_low") # average ratio of lower spikes

graph = plt.bar(categories, values, color = 'red', edgecolor = 'black')
plt.bar_label(graph, fmt = "%.3f", padding = 3)
plt.xlabel("RSI")
plt.ylabel("Ratio of Spikes")
plt.title("Ratio of Spikes When RSI Changes")
plt.show()