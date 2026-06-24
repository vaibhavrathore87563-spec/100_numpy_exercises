#create a Numpy array of size 10 containing numbers from 1 to 10 replace all even num with 0 and print all update array

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])
arr[1]=0
arr[3]=0
arr[5]=0
arr[7]=0
arr[9]=0

print(arr)