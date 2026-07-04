import numpy as np
A = np.array([
         [2,1,3,4],
         [1,0,1,2],
         [3,1,4,6],
         [4,2,7,10]
])
rank = np.linalg.matrix_rank(A)
print(rank)