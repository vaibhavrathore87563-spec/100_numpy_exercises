# How to find the most frequent value in an array?

import numpy as np
arr = np.array([1,2,3,4,1,7,1,8,1,2,3,2,7,9])
most_frequent = np.bincount(arr).argmax()
print(most_frequent)

# .argmax() --> find index of maximum count
# np.bincount()-->It counts how many times each non-negative integer appears in an array.
# output = 1