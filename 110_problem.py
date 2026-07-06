# Consider an array of dimension (5,5,3), how to multiply it by an array with dimensions (5,5)?

import numpy as np
A = np.ones((5,5,3))
print("Array one:",A)
B = np.ones((5,5))
print("Array two:",B)

c = A * B[:, :, None]
print("--------------\n" , c.shape,c)