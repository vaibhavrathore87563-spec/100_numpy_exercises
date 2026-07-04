import numpy as np
A = np.ones((4,4,3))
B = np.arange(16).reshape(4,4)

C  = A * B[:, :, None]

print(C.shape)
print(C) 

print(A.shape)
print(B.shape)

print ( A * B[:, :,None])
print(C[0,0],C[1,2],C[3,3])
