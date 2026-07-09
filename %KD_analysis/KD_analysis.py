import pandas as pd
import os
import sys
# 将dir0加入Python搜索路径
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import tick_data


lowest = tick_data. m1_data['low'].rolling(14).min()
highest = tick_data. m1_data['high'].rolling(14).max()
tick_data. m1_data['%K'] = 100 * (tick_data. m1_data['close'] - lowest) / (highest - lowest)
tick_data. m1_data['%D'] = tick_data. m1_data['%K'].rolling(3).mean()

bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
tick_data. m1_data['range%K'] = pd.cut(tick_data. m1_data['%K'], bins = bins)
countsK_all = tick_data. m1_data['range%K'].value_counts().sort_index()

tick_data. m1_data['range%D'] = pd.cut(tick_data. m1_data['%D'], bins = bins)
countsD_all = tick_data. m1_data['range%D'].value_counts().sort_index()

spikes =  tick_data. m1_data[tick_data. m1_data['spike']]




