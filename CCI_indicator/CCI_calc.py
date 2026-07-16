import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import tick_data


data = tick_data.m1_data
data['typical_price'] = (data['high'] + data['low']+ data['close']) / 3
data['SMA20_TP'] = data['typical_price'].rolling(20).mean() # calculate the sma of TP with a period of 20
data['deviation'] = (data['typical_price'] - data['SMA20_TP']).abs()
data['mean_deviation'] = data['deviation'].rolling(20).mean()

data['CCI'] = (data['typical_price'] - data['SMA20_TP']) / (0.015 * data['mean_deviation']) # calculate the CCI indicator



