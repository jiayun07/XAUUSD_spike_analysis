# analyze whether the continuous decrease of low price gives a changing probability of spikes
import tick_data
import pandas as pd
import matplotlib.pyplot as plt

data = tick_data. m1_data
data['decrease_2'] = (
    (data['low'] < data['low'].shift(1))
    &
    (data['low'].shift(1) < data['low'].shift(2))
) # return whether the lows continually decreases in 2 mins

categories = []
values = []
for i in range(3, 8):
    categories.append(f'decrease_{i - 1}')
    table = pd.crosstab(data['spike_above'], data[f'decrease_{i - 1}']) # can be modified to spike_below
    ratio = table.loc[True, True] / (table.loc[True, True] + table.loc[False, True])  # return P(spike | exceed_i = true)
    values.append(ratio)
    data[f'decrease_{i}'] = (data[f'decrease_{i - 1}'] & (data['low'].shift(i - 1) < data['low'].shift(i)))

categories.append('All Time')
values.append(data['spike_above'].mean()) # can be modified to spike_below
# plot the graph
bars = plt.bar(categories, values, color='skyblue', edgecolor='black')
plt.bar_label(bars, fmt='%.3f', padding=3)
plt.title('Ratio of Spikes Below when the Low Price Decreases')
plt.xlabel('Time Interval')
plt.ylabel('Ratio of Spikes')
plt.show()