import numpy as np
arr = np.array([
           [1,2,0],
           [3,4,0],
           [5,6,0]
])
print((arr ==0).all(axis=0))
print(np.any((arr==0).all(axis=0)))
print(np.where((arr==0).all(axis =0))[0])