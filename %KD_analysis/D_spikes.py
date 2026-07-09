import matplotlib.pyplot as plt
import KD_analysis

countsD_spikes = KD_analysis. spikes['range%D'].value_counts().sort_index()
ratioD = countsD_spikes / KD_analysis. countsD_all
ratioD.plot(kind='bar')
print(ratioD)
plt.xlabel('Intervals')
plt.ylabel('Ratio of spikes')
plt.title('%D spike ticks ratio')
plt.show()