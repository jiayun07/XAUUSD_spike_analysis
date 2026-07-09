import tick_data
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

tick_data. m1_data['exceed_wma_prev'] = (
    (tick_data. m1_data['close'].shift(1) > tick_data. m1_data['WMA10'].shift(1))
    &
    (tick_data. m1_data['close'].shift(2) <= tick_data. m1_data['WMA10'].shift(2)) # price exceeds moving average
)

tick_data. m1_data['drop_wma_prev'] = (
    (tick_data. m1_data['close'].shift(1) < tick_data. m1_data['WMA10'].shift(1))
    &
    (tick_data. m1_data['close'].shift(2) >= tick_data. m1_data['WMA10'].shift(2)) # price drops below moving average
)
table1 = pd.crosstab(tick_data. m1_data['spike'], tick_data. m1_data['exceed_wma_prev'])
chi2, p, dof, expected = chi2_contingency(table1)

n = table1.values.sum()
phi = np.sqrt(chi2 / n)
print(table1)
print("chi2 =", chi2)
print("p =", p)
print("phi =", phi)

table2 = pd.crosstab(tick_data. m1_data['spike'], tick_data. m1_data['drop_wma_prev'])
chi2_2, p_2, dof_2, expected_2 = chi2_contingency(table2)

n_2 = table2.values.sum()
phi_2 = np.sqrt(chi2_2 / n_2)
print(table2)
print("chi2 =", chi2_2)
print("p =", p_2)
print("phi =", phi_2)
'''
pd.set_option('display.max_rows', None)      # 显示所有行
pd.set_option('display.max_columns', None)   # 显示所有列
pd.set_option('display.width', None)         # 自动调整显示宽度
pd.set_option('display.max_colwidth', None)  # 不截断列内容

print(tick_data. m1_data)
'''
