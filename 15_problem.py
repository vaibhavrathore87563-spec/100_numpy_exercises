#Create a 4×4 NumPy matrix using the given values. Find the sum of all elements, the maximum element, the transpose of the matrix, and the sum of the principal diagonal elements

import numpy as np
A = np.array([
    [2,4,6,8],
    [1,3,5,7],
    [9,11,13,15],
    [10,12,14,16]
    ])
print("sum =",np.sum(A))# sum of matrix
print( "Digonal =",np.trace(A))#Digonal sum
print("Max =",np.max(A))#maximum num
print("Min =",np.min(A))#minimum 