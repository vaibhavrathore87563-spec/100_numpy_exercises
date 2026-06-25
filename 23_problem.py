#Create a random integer array of size 15 with values ranging from 1 to 100. Then:

#Find the minimum value in the array.
#Calculate the difference between the maximum and minimum values.

import numpy as np
arr = np.random.randint(1,101,15)

print("Array =",arr)
print("maximum value =",np.max(arr))
print("Minimum value =",np.min(arr))
print("Diffrence value =",np. max (arr) - np.min(arr))