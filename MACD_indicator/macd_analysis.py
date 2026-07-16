
from macd_calc import data
import matplotlib.pyplot as plt
import pandas as pd

bins = []
i = - 2
while -2 <= i <= 2:
    bins.append(i)
    i += 0.4
data['interval'] = pd.cut(data['Histogram'], bins = bins)
counts_all = data['interval'].value_counts().sort_index()
spikes = data[data['spike']]
counts_spike = spikes['interval'].value_counts().sort_index()
ratio = counts_spike / counts_all
print(counts_all)
ratio.plot(kind = 'bar')
plt.xlabel('Intervals')
plt.ylabel('Ratio')
plt.title('Spikes Occurrence in Intervals')
plt.show()

