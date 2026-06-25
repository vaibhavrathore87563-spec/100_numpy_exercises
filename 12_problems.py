import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])

odd = arr[arr % 2 !=0]
print(odd)
