import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import tick_data

data = tick_data. m1_data
data['EMA13'] = data['close'].ewm(span=13, adjust=False).mean()
data['bull_pwr'] = data['high'] - data['EMA13']
data['bear_pwr'] = data['low'] - data['EMA13']
