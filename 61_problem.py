import numpy as np

arr = np.array([1,-2,4,5,6,7,89,-11,-32,12,9,32,4])
print("Original Array:",arr)

arr1 = np.abs(arr)
print("sign remove:",arr)

arr2 = np.sort(arr1)
print("Sort Array:",arr2)

arr3 = np.unique(arr2)
print("Unique sorted array:",arr3)