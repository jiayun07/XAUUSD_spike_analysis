from RSI_calc import data
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

data['high_gain'] = data['high'] - data['open']
data['low_loss'] = data['open'] - data['low']
avg_gain_high = (data['gain'].shift(1).rolling(13).sum() + data['high_gain']) / 14
avg_loss_high = (data['loss'].shift(1).rolling(13).sum()) / 14
avg_gain_low = (data['gain'].shift(1).rolling(13).sum()) / 14
avg_loss_low = (data['loss'].shift(1).rolling(13).sum() + data['low_loss']) / 14

RS_high = avg_gain_high / avg_loss_high
RS_low = avg_gain_low / avg_loss_low
data['RSI_high'] = 100 - 100 / (1 + RS_high)
data['RSI_low'] = 100 - 100 / (1 + RS_low)

data['prev_overselling'] = ((data['RSI_high'].shift(1) > 30) & (data['RSI_low'].shift(1) > 30))
data['prev_overbuying'] = ((data['RSI_high'].shift(1) < 70) & (data['RSI_low'].shift(1) < 70))
data['prev_overselling2'] = (data['prev_overselling'] & (data['RSI_high'].shift(2) > 30) & (data['RSI_low'].shift(2) > 30))
data['prev_overbuying2'] = (data['prev_overselling'] & (data['RSI_high'].shift(2) < 70) & (data['RSI_low'].shift(2) < 70))

table = pd.crosstab(data['spike_below'], data['prev_overselling'])
chi2, p, dof, expected = chi2_contingency(table)

n = table.values.sum()
phi = np.sqrt(chi2 / n)
print(table)
print("chi2 =", chi2)
print("p =", p)
print("phi =", phi) # -1 <= phi <= 1
result1 = table.loc[True, True] / (table.loc[True, True] + table.loc[False, True])
print(f"P(spike | prev_overselling = true) = {result1}")
result2 = table.loc[True, False] / (table.loc[True, False] + table.loc[False, False])
print(f"P(spike | prev_overselling = false) = {result2}")
result3 = result1 / result2 - 1
result3 *= 100
result3 = round(result3, 2)
if result3 >=0:
    print(f"Spike appears {result3}% more frequent after a stick with RSI < 30 all the time.")
else:
    print(f"Spike appears {-result3}% less frequent after a stick with RSI < 30 all the time.")

table = pd.crosstab(data['spike_below'], data['prev_overselling2'])
chi2, p, dof, expected = chi2_contingency(table)

n = table.values.sum()
phi = np.sqrt(chi2 / n)
print(table)
print("chi2 =", chi2)
print("p =", p)
print("phi =", phi) # -1 <= phi <= 1
result1 = table.loc[True, True] / (table.loc[True, True] + table.loc[False, True])
print(f"P(spike | prev_overselling2 = true) = {result1}")
result2 = table.loc[True, False] / (table.loc[True, False] + table.loc[False, False])
print(f"P(spike | prev_overselling2 = false) = {result2}")
result3 = result1 / result2 - 1
result3 *= 100
result3 = round(result3, 2)
if result3 >=0:
    print(f"Spike appears {result3}% more frequent after 2 stick with RSI < 30 all the time.")
else:
    print(f"Spike appears {-result3}% less frequent after 2 stick with RSI < 30 all the time.")

table = pd.crosstab(data['spike_above'], data['prev_overbuying'])
chi2, p, dof, expected = chi2_contingency(table)

n = table.values.sum()
phi = np.sqrt(chi2 / n)
print(table)
print("chi2 =", chi2)
print("p =", p)
print("phi =", phi)  # -1 <= phi <= 1
result1 = table.loc[True, True] / (table.loc[True, True] + table.loc[False, True])
print(f"P(spike | prev_overbuying = true) = {result1}")
result2 = table.loc[True, False] / (table.loc[True, False] + table.loc[False, False])
print(f"P(spike | prev_overbuying = false) = {result2}")
result3 = result1 / result2 - 1
result3 *= 100
result3 = round(result3, 2)
if result3 >= 0:
    print(f"Spike appears {result3}% more frequent after a stick with RSI > 70 all the time.")
else:
    print(f"Spike appears {-result3}% less frequent after a stick with RSI > 70 all the time.")

table = pd.crosstab(data['spike_above'], data['prev_overbuying2'])
chi2, p, dof, expected = chi2_contingency(table)

n = table.values.sum()
phi = np.sqrt(chi2 / n)
print(table)
print("chi2 =", chi2)
print("p =", p)
print("phi =", phi)  # -1 <= phi <= 1
result1 = table.loc[True, True] / (table.loc[True, True] + table.loc[False, True])
print(f"P(spike | prev_overbuying2 = true) = {result1}")
result2 = table.loc[True, False] / (table.loc[True, False] + table.loc[False, False])
print(f"P(spike | prev_overbuying2 = false) = {result2}")
result3 = result1 / result2 - 1
result3 *= 100
result3 = round(result3, 2)
if result3 >= 0:
    print(f"Spike appears {result3}% more frequent after 2 stick with RSI > 70 all the time.")
else:
    print(f"Spike appears {-result3}% less frequent after 2 stick with RSI > 70 all the time.")
