import numpy as np
import sys
import time
o =np.full((2,3),7)
print(o)

o1 =np.full((2,5),np.random.randint(1,10))
print(o1)

o2 = np.random.randint(0,10,size=(3,4))
print(o2)
print(o2.T)