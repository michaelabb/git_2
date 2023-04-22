import numpy as np
import sys
import time

tempratures = np.array([29.3,42.1,18.8,38.0,12.5,12.6,12.7,49.9,38.6,31.3,9.2,22.2]).reshape(2,3,2)
print(tempratures)
print('----------')
tempratures = np.swapaxes(tempratures,1,2)
print(tempratures)
