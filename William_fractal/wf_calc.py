import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import tick_data


data = tick_data.m1_data
data['top'] = (
    (data['high'].shift(2) < data['high'])
    &
    (data['high'].shift(1) < data['high'])
    &
    (data['high'].shift(-1) < data['high'])
    &
    (data['high'].shift(-2) < data['high'])
)

data['bottom'] = (
    (data['low'].shift(2) > data['low'])
    &
    (data['low'].shift(1) > data['low'])
    &
    (data['low'].shift(-1) > data['low'])
    &
    (data['low'].shift(-2) > data['low'])
)

