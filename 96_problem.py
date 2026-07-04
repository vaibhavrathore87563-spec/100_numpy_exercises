#How to swap two coloumn of an array in place?

import numpy as np
arr = np.array([
            [7,8,9],
            [10,11,12],
            [13,14,15]
])

[print("Original array:\n",arr)]

arr[:,[0 , 2]] = arr[:,[2 , 0]]

print("Swapped array:\n",arr)