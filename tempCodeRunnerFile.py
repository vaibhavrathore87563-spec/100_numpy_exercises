import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
arr[arr % 2 == 0] *= 10
print(arr)