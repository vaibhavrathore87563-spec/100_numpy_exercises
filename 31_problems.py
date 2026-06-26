#create a numpy arrays
import numpy as np
arr1 = np.zeros((3,4))
print(arr1,arr1.shape)

arr2 = np.ones((3,3))
print(arr2, arr2.shape)

arr3 = np.full((5,5),8)

print(arr3, arr3.shape)
#matrix in 3x5
arr4 = np.full((5,3),5)
print(arr4, arr4.shape)

# identify  matrix 3x3
 
arr5 = np.eye(3)
print(arr5,arr5.shape)