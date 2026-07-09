# analysis of the difference between SMA period 10 and SMA period 50
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import tick_data
import pandas as pd
import matplotlib.pyplot as plt

tick_data. m1_data['SMA10'] = tick_data. m1_data['close'].rolling(10).mean()
tick_data. m1_data['SMA50'] = tick_data. m1_data['close'].rolling(50).mean()
tick_data. m1_data['gap'] = tick_data. m1_data['SMA10'] - tick_data. m1_data['SMA50'] # calculate the difference between the two line
tick_data. m1_data['diff_from_prev'] = tick_data. m1_data['gap'].shift(1).diff() # calculate the change in gap in the previous two minutes

bins = []
i = -3
while -3 <= i <= 3:
    bins.append(i)
    i += 0.3

tick_data. m1_data['interval'] = pd.cut(tick_data. m1_data['diff_from_prev'], bins = bins)
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
plt.title('SMA difference change between p = 10/50 spike ratio')
plt.show()
