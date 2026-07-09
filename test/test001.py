import pandas as pd

df = pd.read_csv('test/for_test.csv')
df['time_msc'] = pd.to_datetime(df['time_msc'])
df = df.set_index('time_msc')
m1 = df['bid'].resample("1Min").ohlc() # 1 分钟k线
m1['return'] = m1['close'] - m1['open'] # 1分钟涨跌
m1['abs_return'] = m1['return'].abs() # 涨跌幅度
m1['spike'] = (m1['abs_return'] < 0.33 * (m1['high'] - m1['low']))
# 实体顶部和底部
body_high = m1[['open', 'close']].max(axis=1)
body_low = m1[['open', 'close']].min(axis=1)

# 上影线
m1['upper_shadow'] = m1['high'] - body_high

# 下影线
m1['lower_shadow'] = body_low - m1['low']
m1['is_higher'] = (m1['close'] > m1['close'].shift(1))
pd.set_option('display.max_rows', None)      # 显示所有行
pd.set_option('display.max_columns', None)   # 显示所有列
pd.set_option('display.width', None)         # 自动调整显示宽度
pd.set_option('display.max_colwidth', None)  # 不截断列内容

print(m1)

'''
# print(m1.query("spike"))
# print(m1.loc['2026-01-26 01:07:00'])
spikes = m1.loc[m1['spike']]
# print(len(spikes))
spikes['hour'] = spikes.index.hour
# print(spikes.groupby('hour').size())
'''
