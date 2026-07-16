from RSI_calc import data
import pandas as pd
import matplotlib.pyplot as plt


data['prev_diff'] = data['RSI'].shift(1).diff()

bins = [-50, -45, -40, -35, -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

data['interval'] = pd.cut(data['prev_diff'], bins = bins)
counts1 = data['interval'].value_counts().sort_index()
print(counts1)
spikes = data[data['spike']]
counts2 = spikes['interval'].value_counts().sort_index()
print(counts2)
ratio = counts2 / counts1
print(ratio)
az = ratio.plot(kind='bar')
plt.xlabel('Difference from previous')
plt.ylabel('Ratio')
plt.title('RSI difference spike ratio')
plt.show()