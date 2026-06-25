
# print non zero num
import numpy as np

arr = np.array([1,2,3,4,5])
indices = np.nonzero(arr)
print(indices)
print(arr[np.nonzero(arr)])

