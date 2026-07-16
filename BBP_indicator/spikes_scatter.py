import matplotlib.pyplot as plt
from BBP_calc import data

spikes = data[data['spike']]
bull_power = spikes['bull_pwr']
bear_power = spikes['bear_pwr']

plt.scatter(bull_power, bear_power, color = 'skyblue')
plt.xlabel('Bull Power')
plt.ylabel('Bear Power')
plt.title('Bull/Bear Powers of Spikes')
plt.show()