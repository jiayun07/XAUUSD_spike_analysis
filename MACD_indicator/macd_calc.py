import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import tick_data

data = tick_data. m1_data
data['MACD'] = data['close'].ewm(span = 12, adjust= False).mean() - data['close'].ewm(span = 26, adjust= False).mean()
data['signal'] = data['MACD'].ewm(span = 9, adjust= False).mean()
data['Histogram'] = data['MACD'] - data['signal']