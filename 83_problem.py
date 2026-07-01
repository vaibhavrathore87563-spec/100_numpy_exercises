import numpy as np
Z = np.array([
    [5,2,8],
    [1,9,3],
    [4,6,7]

])
n = 2
print(Z)

Z=Z[Z[:,n].argsort()]
print(Z)