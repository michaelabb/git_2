import numpy as np
import sys
import time

a1 = np.array([1,2,3,4,5,6])
a2 = np.array([1,2,3,9,3,6])

print(np.product(a1>a2))
print(np.where(a1==a2))
print(np.where(a1>a2))