#Given the following NumPy array:

#arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

#Without using loops, multiply all even numbers in the array by 10 using Boolean Indexing and print the updated array.

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
arr[arr % 2 == 0] *= 10
print(arr)