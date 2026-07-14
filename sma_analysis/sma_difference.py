import pandas as pd
import matplotlib.pyplot as plt
from sma import data

bins = []
i = -3
while -3 <= i <= 3:
    bins.append(i)
    i += 0.3

data['interval'] = pd.cut(data['diff_from_prev'], bins = bins)
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
plt.title('SMA difference change between p = 10/50 spike ratio')
plt.show()