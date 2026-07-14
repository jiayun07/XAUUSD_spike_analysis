# analysis of the difference of value between SMA p = 10 and p = 50
from sma import data
import pandas as pd
import matplotlib.pyplot as plt

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
data['interval'] = pd.cut(data['gap'], bins = bins)
counts_all = data['interval'].value_counts().sort_index()
spikes = data[data['spike']]
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