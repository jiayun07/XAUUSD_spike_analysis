import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np
import tick_data

price = tick_data. m1_data['close']
nearest = round(price)
distance = abs(price - nearest)
tick_data. m1_data['near_integer'] = (distance <= 0.2) # 检测是否靠近整数
table = pd.crosstab(tick_data. m1_data['spike'], tick_data. m1_data['near_integer'])
chi2, p, dof, expected = chi2_contingency(table)

n = table.values.sum()
phi = np.sqrt(chi2 / n)
print(table)
print("chi2 =", chi2)
print("p =", p)
print("phi =", phi) # -1 <= phi <= 1