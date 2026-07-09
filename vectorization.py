#Addition

import numpy as np
arr = np.array([1,2,3,4,5])
arr1 = np.array([11,12,13,14,15])

C = (arr +arr1)
print(C)

a = np.array([1,2,3])
print(a + 6)

# Mulitiplication

arr = np.array([2,3,4,5])
print(arr*10)

#Element wise ope ration-,

a = np.array([1,2,3])
b = np.array([4,5,6])
C =(a * b)
print(C)


#Mathematical Function(Square root)

import numpy as np
arr = np.array([1,2,33,625])
print(np.sqrt(arr))

# conditional operator

a = np.array([10,20,30,40,50])
print(a > 18)
print(a[a>18])