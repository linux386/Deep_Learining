
import numpy as np

# build datasets
def build_dataset(data):
  for i in range(0, len(time_series) - seq_length):
    _x = time_series[i:i + seq_length, :]
    _y = time_series[i + seq_length, [-1]]  # Next close price
    print(_x, "->", _y)
    dataX.append(_x)
    dataY.append(_y)
    return np.array(dataX), np.array(dataY)
