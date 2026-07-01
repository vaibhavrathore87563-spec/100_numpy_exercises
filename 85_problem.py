#How to tell if a given 2D array has null rows, and how to find their indices?"
import numpy as np
arr = np.array([
           [0,0,0],
           [1,2,3],
           [0,0,0],
           [4,5,6]
])
print((arr == 0).all (axis = 1))
print(np.any((arr==0).all(axis=1)))
print(np.where((arr ==0).all(axis=1)))