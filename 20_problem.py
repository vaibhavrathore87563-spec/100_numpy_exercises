#Given a NumPy array, find the indices of all non-zero elements and calculate the sum of the non-zero values without using any loops.

import numpy as np
arr1 = np.array([0, 12, 0, 18, 20, 0, 25, 0])
indices = np.nonzero(arr1)
print(indices)
print("sum =",np.sum(arr1))