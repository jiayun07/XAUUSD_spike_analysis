import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import tick_data
import pandas as pd
import matplotlib.pyplot as plt

data = tick_data.m1_data
data['typical_price'] = (data['high'] + data['low']+ data['close']) / 3
data['SMA20_TP'] = data['typical_price'].rolling(20).mean() # calculate the sma of TP with a period of 20
data['deviation'] = (data['typical_price'] - data['SMA20_TP']).abs()
data['mean_deviation'] = data['deviation'].rolling(20).mean()

data['CCI'] = (data['typical_price'] - data['SMA20_TP']) / (0.015 * data['mean_deviation']) # calculate the CCI indicator

bins = []
i = -200
while i <= 200:
    bins.append(i)
    i += 40

data['interval'] = pd.cut(data['CCI'], bins = bins)
before_spikes = data[data['spike']].shift(1)
counts_all = data['interval'].value_counts().sort_index()
counts_spikes = before_spikes['interval'].value_counts().sort_index()
ratio = counts_spikes / counts_all
print(counts_all)
print(ratio)
ratio.plot(kind = 'bar')
plt.xlabel('Difference from previous')
plt.ylabel('Ratio')
plt.title('SMA difference change between p = 10/50 spike ratio')
plt.show()

