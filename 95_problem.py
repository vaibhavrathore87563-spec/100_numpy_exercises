# How to swap two rows of an array in place ?

import numpy as np
arr = np.array([
         [1,2,3],
         [4,5,6],
         [7,8,9]
])
print("Normal arr:\n",arr)
arr[[0,1]] = arr[[1,0]]
print("Swapped arr:\n",arr)