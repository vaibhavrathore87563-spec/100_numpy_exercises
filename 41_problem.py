#Given the following NumPy array:

#arr = np.array([2, 5, 8, 1, 9, 4, 7])

#Without using loops, make all elements greater than 5 negative using Boolean Indexing and print the updated array.

import numpy as np
arr = np.array([2,5,8,1,9,4,7])

arr[arr > 5]*=-1
print(arr)


import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
arr[arr % 2 == 0] *= 10
print(arr)