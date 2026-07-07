#convert 2D Array into 1D Array 2D => 1D
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])

flattened = arr.flatten() # 2D=> 1D
print(flattened,flattened.shape)