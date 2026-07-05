import numpy as np
arr = np.ones((18,18))
result= arr.reshape(3,6,3,6).sum(axis=(1,3))
print(result)