import numpy as np
arr1 = np.array([10, 0, 20, 0, 30, 40, 0])
indices = np.nonzero(arr1)
print(indices)
print(arr1[np.nonzero(arr1)])