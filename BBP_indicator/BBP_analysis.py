# analyze whether spikes occurs more when the bull/bear power changes sign
from BBP_calc import data
import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np

data['bull_down'] = (
    (data['bull_pwr'].shift(1) > 0)
    &
    (data['bull_pwr'] < 0)
) # return whether bull power changes from + to -

data['bear_up'] = (
    (data['bear_pwr'].shift(1) < 0)
    &
    (data['bear_pwr'] > 0)
) # return whether bear power changes from - to +

table = pd.crosstab(data['spike'], data['bear_up'])
chi2, p, dof, expected = chi2_contingency(table)

n = table.values.sum()
phi = np.sqrt(chi2 / n)
print(table)
print("chi2 =", chi2)
print("p =", p)
print("phi =", phi) # -1 <= phi <= 1
result1 = table.loc[True, True] / (table.loc[True, True] + table.loc[False, True])
print(f"P(spike | bear - to + = true) = {result1}")
result2 = table.loc[True, False] / (table.loc[True, False] + table.loc[False, False])
print(f"P(spike | bear - to + = false) = {result2}")
result3 = result1 / result2 - 1
result3 *= 100
result3 = round(result3, 2)
if result3 >= 0:
    print(f"Spike appears {result3}% more frequent after bear power changes from - to +.")
else:
    print(f"Spike appears {-result3}% less frequent after bear power changes from - to +.")

table = pd.crosstab(data['spike'], data['bull_down'])
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
if result3 >=0:
    print(f"Spike appears {result3}% more frequent after bull power changes from + to -.")
else:
    print(f"Spike appears {-result3}% less frequent after bull power changes from + to -.")
