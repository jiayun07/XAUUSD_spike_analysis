import KD_analysis
import matplotlib.pyplot as plt

countsK_spikes = KD_analysis. spikes['range%K'].value_counts().sort_index()
ratioK = countsK_spikes / KD_analysis. countsK_all
ratioK.plot(kind='bar')
print(ratioK)
plt.xlabel('Intervals')
plt.ylabel('Ratio of spikes')
plt.title('%K spike ticks ratio')
plt.show()