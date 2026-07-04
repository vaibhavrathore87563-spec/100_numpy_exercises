#How to create a 4X4 array and swap the first and last row?

import numpy as np
arr = np.array([
            [23,24,25,26],
            [15,16,17,18],
            [19,20,21,22],
            [11,12,13,14]
])
print("normal array:\n",arr)
arr[[0,3]] = arr[[3,0]]
print("Swapped array:\n",arr)