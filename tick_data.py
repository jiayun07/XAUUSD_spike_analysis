import pandas as pd
import glob
import numpy as np
files = glob.glob("data/*.csv")

m1_list = []

for file in files:

    df = pd.read_csv(file)

    df['time_msc'] = pd.to_datetime(df['time_msc'])

    df = df.set_index('time_msc')

    m1 = df['bid'].resample('1Min').ohlc() # m1为一分钟k线表
    m1['body'] = m1['open'] - m1['close']  # 实体
    m1['abs_body'] = m1['body'].abs()  # 实体长度
    m1['body_high'] = m1[['open', 'close']].max(axis = 1) # axis = 1 表横向计算
    m1['body_low'] = m1[['open', 'close']].min(axis = 1)
    m1['upper_shadow'] = m1['high'] - m1['body_high']
    m1['lower_shadow'] = m1['body_low'] - m1['low']
    m1['spike'] = (
            (
                    (m1['upper_shadow'] >= 2 * m1['abs_body'])
                    &
                    (m1['lower_shadow'] < 0.1 * (m1['high'] - m1['low']))
            )
            |
            (
                            (m1['lower_shadow'] >= 2 * m1['abs_body'])
                            &
                            (m1['upper_shadow'] < 0.1 * (m1['high'] - m1['low']))
            )
    )
    window = 10 # 计算移动平均线
    weights = np.arange(1, window + 1)
    m1['WMA10'] = (m1['close'].rolling(window).apply(lambda x: np.dot(x, weights)/ weights.sum(), raw = True)) # weighted moving average
    m1_list.append(m1)

m1_data = pd.concat(m1_list)
m1_data = m1_data.sort_index()
m1_data.dropna(subset = ['open', 'close'], inplace = True) # drop empty ticks (00:00 - 01:00)
'''
pd.set_option('display.max_rows', None)      # 显示所有行
pd.set_option('display.max_columns', None)   # 显示所有列
pd.set_option('display.width', None)         # 自动调整显示宽度
pd.set_option('display.max_colwidth', None)  # 不截断列内容
print(m1_data)
'''




