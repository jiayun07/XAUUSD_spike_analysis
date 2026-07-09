import pandas as pd
'''
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
# Cuts data into 3 equal-width intervals
custom_edges = [0, 18, 35, 60, 100]
custom_bins = pd.cut(ages, bins=custom_edges)
print(custom_bins)
'''
# Sample data
df = pd.DataFrame({'sales': [10, 21, 33, 46, 50, 60]})

# Calculate a 3-row rolling mean
df['prev2_diff'] = df['sales'].shift(2).diff()
print(df)
