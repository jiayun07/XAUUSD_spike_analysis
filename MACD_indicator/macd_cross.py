import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import tick_data
import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np

data = tick_data. m1_data
span = 12
span2 = 26
data['EMA12'] = None # ema when the price riches the highest point at the time
data['EMA26'] = None
'''
for i in range(span - 1, len(data)):
    values = pd.concat([data['close'].iloc[i - span + 1 : i], data['high'].iloc[[i]]])
    data.loc[data.index[i], 'EMA12'] = (
        values.ewm(span=span, adjust=False).mean().iloc[-1]
    )
    if i >= span2 - 1:
        values = pd.concat([data['close'].iloc[i - span2 + 1: i], data['high'].iloc[[i]]])
        data.loc[data.index[i], 'EMA26'] = (
            values.ewm(span=span2, adjust=False).mean().iloc[-1]
        )
''' # this algorithm runs is too slow
alpha = 2 / (span + 1)
alpha2 = 2 / (span2 + 1)
ema_close = data['close'].ewm(span=span, adjust=False).mean()
data['EMA12'] = (
    alpha * data['high']
    + (1 - alpha) * ema_close.shift(1)
)
ema_close2 = data['close'].ewm(span=span2, adjust=False).mean()
data['EMA26'] = (
    alpha2 * data['high']
    + (1 - alpha2) * ema_close2.shift(1)
)

data['high_MACD'] = data['EMA12'] - data['EMA26']
data['high_signal'] = data['high_MACD'].ewm(span = 9, adjust = False).mean()
data['gold_cross'] = (
    (data['high_MACD'].shift(1)  < data['high_signal'].shift(1))
    &
    (data['high_MACD'] > data['high_signal'])
)

table = pd.crosstab(data['spikes'], data['gold_cross'])
chi2, p, dof, expected = chi2_contingency(table)

n = table.values.sum()
phi = np.sqrt(chi2 / n)
print(table)
print("chi2 =", chi2)
print("p =", p)
print("phi =", phi) # -1 <= phi <= 1
result1 = table.loc[True, True] / (table.loc[True, True] + table.loc[False, True])
print(f"P(spike | bull + to - = true) = {result1}")
result2 = table.loc[True, False] / (table.loc[True, False] + table.loc[False, False])
print(f"P(spike | bull + to - = false) = {result2}")
result3 = result1 / result2 - 1
result3 *= 100
result3 = round(result3, 2)
if result3 >= 0:
    print(f"Spike appears {result3}% more frequent when gold cross occurs.")
else:
    print(f"Spike appears {-result3}% less frequent when gold cross occurs.")
