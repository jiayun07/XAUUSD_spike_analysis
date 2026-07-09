import pandas as pd
import glob

files = glob.glob("data/*.csv")

m1_list = []

for file in files:

    df = pd.read_csv(file)

    df['time_msc'] = pd.to_datetime(df['time_msc'])

    df = df.set_index('time_msc')

    m1 = df['bid'].resample('1Min').ohlc()
    m1['return'] = m1['close'] - m1['open']  # 1分钟涨跌 m1['close'].diff()不考虑跳空
    m1['abs_return'] = m1['return'].abs()   # 幅度
    std = m1['return'].std()
    m1['spike'] = (
            m1['abs_return'] > 3 * std
    )
    m1_list.append(m1)

m1_data = pd.concat(m1_list)

m1_data = m1_data.sort_index()

spikes = m1_data.loc[m1_data['spike']]
spikes['hour'] = spikes.index.hour
print(spikes.groupby('hour').size())