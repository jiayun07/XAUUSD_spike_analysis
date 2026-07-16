# analyse if previous sma cross the body affect the occurrence of spike in the next min
import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np
from sma_calc import data

data['prev_cross'] = (
    (
        (data['close'].shift(1) <= data['SMA50'].shift(1))
        &
        (data['SMA50'].shift(1) <= data['open'].shift(1))
    )
    |
    (
        (data['open'].shift(1) <= data['SMA50'].shift(1))
        &
        (data['SMA50'].shift(1) <= data['close'].shift(1))
    )
) # check if the previous SMA50 crosses the body
'''
prev1_cross = (
    (
        (data['close'].shift(1) <= data['SMA50'].shift(1))
        &
        (data['SMA50'].shift(1) <= data['open'].shift(1))
    )
    |
    (
        (data['open'].shift(1) <= data['SMA50'].shift(1))
        &
        (data['SMA50'].shift(1) <= data['close'].shift(1))
    )
)
prev2_cross = (
    (
        (data['close'].shift(2) <= data['SMA50'].shift(2))
        &
        (data['SMA50'].shift(2) <= data['open'].shift(2))
    )
    |
    (
        (data['open'].shift(2) <= data['SMA50'].shift(2))
        &
        (data['SMA50'].shift(2) <= data['close'].shift(2))
    )
)

data['prev_cross'] = prev1_cross & prev2_cross # true if SAM50 crosses the body both 1 min and 2 min before
'''
table = pd.crosstab(data['spike'], data['prev_cross'])
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
if result3 >= 0:
    print(f"Spike appears {result3}% more frequent after SMA50 crosses the body.")
else:
    print(f"Spike appears {-result3}% less frequent after SMA50 crosses the body.")