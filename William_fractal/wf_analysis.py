# analyse if spike appears more frequent at local peaks and valleys when the William fractal is used
import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np
from wf_calc import data

spikes = data[data['spike']]
table = pd.crosstab(data['spike'], data['top'])
chi2, p, dof, expected = chi2_contingency(table)

n = table.values.sum()
phi = np.sqrt(chi2 / n)
print(table)
print("chi2 =", chi2)
print("p =", p)
print("phi =", phi) # -1 <= phi <= 1
result1 = table.loc[True, True] / (table.loc[True, True] + table.loc[False, True])
print("P(spike | top = true) = " + str(result1))
result2 = table.loc[True, False] / (table.loc[True, False] + table.loc[False, False])
print("P(spike | top = false) = " + str(result2))
result3 = result1 / result2 - 1
result3 *= 100
result3 = round(result3, 2)
print("Spike appears " + str(result3) + "% more frequent at local peaks.")

table = pd.crosstab(data['spike'], data['bottom'])
chi2, p, dof, expected = chi2_contingency(table)

n = table.values.sum()
phi = np.sqrt(chi2 / n)
print(table)
print("chi2 =", chi2)
print("p =", p)
print("phi =", phi) # -1 <= phi <= 1
result1 = table.loc[True, True] / (table.loc[True, True] + table.loc[False, True])
print("P(spike | bottom = true) = " + str(result1))
result2 = table.loc[True, False] / (table.loc[True, False] + table.loc[False, False])
print("P(spike | bottom = false) = " + str(result2))
result3 = result1 / result2 - 1
result3 *= 100
result3 = round(result3, 2)
print("Spike appears " + str(result3) + "% more frequent at local valleys.")