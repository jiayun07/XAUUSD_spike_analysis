import pandas as pd
'''
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
# Cuts data into 3 equal-width intervals
custom_edges = [0, 18, 35, 60, 100]
custom_bins = pd.cut(ages, bins=custom_edges)
print(custom_bins)
'''
# Sample data
df = pd.DataFrame({'sales': [True, False, True, False, False, True]})


df['prev2_diff'] = df[df['sales'].shift(-1)]
print(df)
