#Explain how NumPy broadcasting works in this statement: (broadcasting + [:, None]

import numpy as np

X = np.array([2,4,6])
Y = np. array([1,3,5,7])

C = X[:,None]+ Y
print(C)
