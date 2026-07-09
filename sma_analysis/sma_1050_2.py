# analysis of the difference of value between SMA p = 10 and p = 50
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import tick_data
import pandas as pd
import matplotlib.pyplot as plt

tick_data. m1_data['SMA10'] = tick_data. m1_data['close'].rolling(10).mean()
tick_data. m1_data['SMA50'] = tick_data. m1_data['close'].rolling(50).mean()
tick_data. m1_data['gap'] = tick_data. m1_data['SMA10'] - tick_data. m1_data['SMA50'] # calculate the difference between the two line


bins = []
'''
i = -60
while -60 <= i <= 60:
    bins.append(i)
    i += 5
'''
i = -3
while -3 <= i <= 3:
    bins.append(i)
    i += 0.3
tick_data. m1_data['interval'] = pd.cut(tick_data. m1_data['gap'], bins = bins)
counts_all = tick_data. m1_data['interval'].value_counts().sort_index()
spikes = tick_data. m1_data[tick_data. m1_data['spike']]
counts_spikes = spikes['interval'].value_counts().sort_index()
print(counts_all)
print(counts_spikes)
ratio = counts_spikes / counts_all
print(ratio)
ratio.plot(kind = 'bar')
plt.xlabel('Difference from previous')
plt.ylabel('Ratio')
plt.title('SMA difference between p = 10/50 spike ratio')
plt.show()