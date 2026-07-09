# check whether spikes appears more frequently after two opposite sign body
import tick_data
import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np

data = tick_data.m1_data
data['is_white'] = (data['body'] > 0)
data['prev_opposite'] = ((
    data['is_white'].shift(1)
)
^
(data['is_white'].shift(2))
)

table = pd.crosstab(data['spike'], data['prev_opposite'])
chi2, p, dof, expected = chi2_contingency(table)

n = table.values.sum()
phi = np.sqrt(chi2 / n)
print(table)
print("chi2 =", chi2)
print("p =", p)
print("phi =", phi) # -1 <= phi <= 1