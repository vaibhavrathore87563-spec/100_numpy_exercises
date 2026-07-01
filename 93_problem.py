import numpy as np
A = np.ones((5,5,3))
print("Array one",A)
B = np.ones((5,5))
print("Array two",B)


C = A * B[:, :, None]

print("--------------\n",C.shape,C)