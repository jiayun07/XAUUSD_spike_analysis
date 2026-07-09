import tick_data
import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np


tick_data. m1_data['previous_is_spike'] = tick_data. m1_data['spike'].shift(1)
table = pd.crosstab(tick_data. m1_data['previous_is_spike'], tick_data. m1_data['spike'])

chi2, p, dof, expected = chi2_contingency(table)

n = table.values.sum()
phi = np.sqrt(chi2 / n)
print(table)
print("chi2 =", chi2)
print("p =", p)
print("phi =", phi) # -1 <= phi <= 1
