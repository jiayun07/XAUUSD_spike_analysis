from CCI_calc import data
import pandas as pd
import matplotlib.pyplot as plt

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