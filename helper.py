
import numpy as np
import pandas as pd

# build datasets
def load_data(data, seq):
    dataX = []
    dataY = []
    for  i in range(num-seq):
        x = xy[i:seq+i]
        y = xy[i+seq, -1]
        lastX  = xy[-seq:]
        dataX.append(x)
        dataY.append(y)
    dataX = np.array(dataX)
    dataY = np.array(dataY)
    return dataX, dataY, lastX 

