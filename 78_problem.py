# How to convert a float (32 bits) array into an integer (32 bits) array in place?

import numpy as np
arr = np.array([1.5, 2.7, 3.9])
print("Original array:",arr)
print(arr.astype(np.int32))

print("converted arr: ",arr)