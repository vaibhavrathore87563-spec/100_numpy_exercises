# Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3 consecutive zeros interleaved between each value?

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Actual array:",arr)
seperate_arr = np.zeros((len(arr) + (len(arr)-1)*3))
seperate_arr[::4]=4
print("Seperate by 000",seperate_arr)
