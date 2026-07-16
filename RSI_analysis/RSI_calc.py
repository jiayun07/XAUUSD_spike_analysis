import os
import sys
# 导入上级目录
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import tick_data
import pandas as pd


tick_data. m1_data['gain'] = tick_data. m1_data['body'].clip(lower = 0)
tick_data. m1_data['loss'] = - tick_data. m1_data['body'].clip(upper = 0)

average_gain= tick_data. m1_data['gain'].rolling(14).mean()
average_loss = tick_data. m1_data['loss'].rolling(14).mean()

RS = average_gain / average_loss
tick_data. m1_data['RSI'] = 100 - 100 / (1 + RS)
data = tick_data. m1_data

'''
ax = counts_all.plot(kind='bar')
for i, v in enumerate(counts_all):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom')
plt.xlabel('Intervals')
plt.ylabel('Number')
plt.title('RSI for all ticks')
plt.show()

ay = counts_spikes.plot(kind='bar')
for i, v in enumerate(counts_spikes):
    ay.text(i, v + 0.1, str(v), ha='center', va='bottom')
plt.xlabel('Intervals')
plt.ylabel('Number')
plt.title('RSI for spike ticks')
plt.show()


'''


