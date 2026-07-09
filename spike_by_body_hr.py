import tick_data
import matplotlib.pyplot as plt

spikes = tick_data. m1_data.loc[tick_data. m1_data['spike']] # about 13123/ 166942 = 7.86% are spikes
'''
print(spikes.info())
print(tick_data. m1_data.info())
'''
spikes['hour'] = spikes.index.hour
hour_counts = spikes.groupby('hour').size()

plt.figure(figsize=(10, 5))

bars = plt.bar(hour_counts.index, hour_counts.values)

# 在柱子顶部显示数值
plt.bar_label(bars, fmt='%d', padding=3)

plt.xlabel('Hour of Day')
plt.ylabel('Number of Spikes')
plt.title('XAUUSD Spike Distribution by Hour')

plt.xticks(range(24))
plt.grid(axis='y')

plt.show()
