# analyze whether the continuous increase of high price gives a changing probability of spikes
import tick_data
import pandas as pd
import matplotlib.pyplot as plt

data = tick_data. m1_data
data['exceed_2'] = (
    (data['high'] > data['high'].shift(1))
    &
    (data['high'].shift(1) > data['high'].shift(2))
) # return whether the highs continually increases in 2 mins

categories = []
values = []
for i in range(3, 8):
    categories.append(f'exceed_{i - 1}')
    table = pd.crosstab(data['spike_below'], data[f'exceed_{i - 1}']) # can be modified to spike_below
    ratio = table.loc[True, True] / (table.loc[True, True] + table.loc[False, True])  # return P(spike | exceed_i = true)
    values.append(ratio)
    data[f'exceed_{i}'] = (data[f'exceed_{i - 1}'] & (data['high'].shift(i - 1) > data['high'].shift(i)))

categories.append('All Time')
values.append(data['spike_below'].mean()) # can be modified to spike_below
# plot the graph
bars = plt.bar(categories, values, color='skyblue', edgecolor='black')
plt.bar_label(bars, fmt='%.3f', padding=3)
plt.title('Ratio of Spikes Below when the High Price Increases')
plt.xlabel('Time Interval')
plt.ylabel('Ratio of Spikes')
plt.show()