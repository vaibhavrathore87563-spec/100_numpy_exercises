# indexing on 2D Arrays
import numpy as np
arr = np.array([[1,2,3],[5,6,7]])

print(arr[0][1])
print(arr[1][1])


#1D indexing normal indexing
import numpy as np
arr =np.array([11,12,13,14,15,16])
print(arr[0])
print(arr[2])



# Fancy indxing
import numpy as np
arr = np.array([1,2,3,4,5,6])

idx = [1,3,5]
print(arr[idx])