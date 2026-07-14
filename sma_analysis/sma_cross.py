# check if the frequency of occurrence of spike changes after two sma lines crosses each other
from sma import data
import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np

data['is_gold_cross'] = (
    (data['SMA10'].shift(1) >= data['SMA50']. shift(1))
    &
    (data['SMA10'] < data['SMA50'])
)

data['is_dead_cross'] = (
    (data['SMA10'].shift(1) < data['SMA50']. shift(1))
    &
    (data['SMA10'] >= data['SMA50'])
)

table = pd.crosstab(data['spike'], data['is_gold_cross'].shift(1))
chi2, p, dof, expected = chi2_contingency(table)

n = table.values.sum()
phi = np.sqrt(chi2 / n)
print(table)
print("chi2 =", chi2)
print("p =", p)
print("phi =", phi) # -1 <= phi <= 1
result1 = table.loc[True, True] / (table.loc[True, True] + table.loc[False, True])
print(f"P(spike | prev_cross = true) = {result1}")
result2 = table.loc[True, False] / (table.loc[True, False] + table.loc[False, False])
print(f"P(spike | prev_cross = false) = {result2}")
result3 = result1 / result2 - 1
result3 *= 100
result3 = round(result3, 2)
if result3 >=0:
    print(f"Spike appears {result3}% more frequent after SMA50 exceeds SMA10.")
else:
    print(f"Spike appears {-result3}% less frequent after SMA50 exceeds SMA10.")

table = pd.crosstab(data['spike'], data['is_dead_cross'].shift(1))
chi2, p, dof, expected = chi2_contingency(table)

n = table.values.sum()
phi = np.sqrt(chi2 / n)
print(table)
print("chi2 =", chi2)
print("p =", p)
print("phi =", phi) # -1 <= phi <= 1
result1 = table.loc[True, True] / (table.loc[True, True] + table.loc[False, True])
print(f"P(spike | prev_cross = true) = {result1}")
result2 = table.loc[True, False] / (table.loc[True, False] + table.loc[False, False])
print(f"P(spike | prev_cross = false) = {result2}")
result3 = result1 / result2 - 1
result3 *= 100
result3 = round(result3, 2)
if result3 >=0:
    print(f"Spike appears {result3}% more frequent after SMA50 exceeds SMA10.")
else:
    print(f"Spike appears {-result3}% less frequent after SMA50 exceeds SMA10.")