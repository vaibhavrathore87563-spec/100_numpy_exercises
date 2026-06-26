#How to find common values between three arrays?
import numpy as np
a = np.array([5,10,15,20,25])
b = np.array([10,20,30,40,50])
c = np.array([10,20,7,6])

result = np.intersect1d(np.intersect1d(a, b),
c)
print(result)