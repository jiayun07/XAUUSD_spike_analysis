# analysis of the difference between SMA period 10 and SMA period 50
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import tick_data

data = tick_data.m1_data
data['SMA10'] = data['close'].rolling(10).mean()
data['SMA20'] = data['close'].rolling(20).mean()
data['SMA50'] = data['close'].rolling(50).mean()
data['gap'] = data['SMA10'] - data['SMA50'] # calculate the difference between the two line
data['diff_from_prev'] = data['gap'].shift(1).diff() # calculate the change in gap in the previous two minutes


