# Create a 2d array with 1 on the border and 0 inside

import numpy as np
arr = np.zeros((5,5),dtype = int)

arr[0,:]=1
arr[-1,:]=1
arr[:,0,]=1
arr[:,-1]=1

print(arr)