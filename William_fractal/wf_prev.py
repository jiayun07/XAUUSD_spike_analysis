# analyse if spike appears more frequent after local peaks and valleys when the William fractal is used
from wf_calc import data
import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np

data['prev_top'] = data['top'].shift(1)
data['prev_bottom'] = data['bottom'].shift(1)
spikes = data[data['spike']]

table = pd.crosstab(data['spike'], data['prev_top'])
chi2, p, dof, expected = chi2_contingency(table)

n = table.values.sum()
phi = np.sqrt(chi2 / n)
print(table)
print("chi2 =", chi2)
print("p =", p)
print("phi =", phi) # -1 <= phi <= 1
result1 = table.loc[True, True] / (table.loc[True, True] + table.loc[False, True])
print(f"P(spike | prev_top = true) = {result1}")
result2 = table.loc[True, False] / (table.loc[True, False] + table.loc[False, False])
print(f"P(spike | prev_top = false) = {result2}")
result3 = result1 / result2 - 1
result3 *= 100
result3 = round(result3, 2)
if result3 >=0:
    print(f"Spike appears {result3}% more frequent after local peaks.")
else:
    print(f"Spike appears {-result3}% less frequent after local peaks.")

table = pd.crosstab(data['spike'], data['prev_bottom'])
chi2, p, dof, expected = chi2_contingency(table)

n = table.values.sum()
phi = np.sqrt(chi2 / n)
print(table)
print("chi2 =", chi2)
print("p =", p)
print("phi =", phi) # -1 <= phi <= 1
result1 = table.loc[True, True] / (table.loc[True, True] + table.loc[False, True])
print("P(spike | prev_bottom = true) = " + str(result1))
result2 = table.loc[True, False] / (table.loc[True, False] + table.loc[False, False])
print("P(spike | prev_bottom = false) = " + str(result2))
result3 = result1 / result2 - 1
result3 *= 100
result3 = round(result3, 2)
if result3 >=0:
    print(f"Spike appears {result3}% more frequent after local valleys.")
else:
    print(f"Spike appears {-result3}% less frequent after local valleys.")