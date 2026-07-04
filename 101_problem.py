# compute a matrix rank
import numpy as np
A = np.array([
            [1,2],
            [2,4]

])
rank = np.linalg.matrix_rank(A)
print(rank)

# compute a matrix rank
import numpy as np
A = np.array([
            [1,2,3,1,0],
            [2,4,6,2,0],
            [1,1,1,0,1],
            [3,5,7,2,1],
            [4,6,8,2,2]       
])

rank = np.linalg.matrix_rank(A)
print(rank)