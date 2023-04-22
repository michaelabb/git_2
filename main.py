import numpy as np
import sys
import time


size = 10000000
l1 = range(size)
l2 = range(size)
a1=np.arange(size)
a2=np.arange(size)
start = time.time()
# result = [(x+y) for (x,y) in zip(l1,l2)]
result =a1+a2
print(result)
end = time.time()
print('time:',end-start)