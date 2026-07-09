import RSI_analysis
import pandas as pd
import matplotlib.pyplot as plt
bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

RSI_analysis. tick_data. m1_data['interval'] = pd.cut(RSI_analysis. tick_data. m1_data['RSI'], bins = bins)
counts_all = RSI_analysis. tick_data. m1_data['interval'].value_counts().sort_index()
#print(counts_all)

spikes = RSI_analysis. tick_data. m1_data[RSI_analysis. tick_data. m1_data['spike']]
counts_spikes = spikes['interval'].value_counts().sort_index()
#print(counts_spikes)

ratio = counts_spikes / counts_all
print(ratio)
az = ratio.plot(kind='bar')
# for i, v in enumerate(ratio):
    # az.text(i, v + 0.1, str(v), ha='center', va='bottom')
plt.xlabel('Intervals')
plt.ylabel('Number')
plt.title('RSI spike ticks ratio')
plt.show()