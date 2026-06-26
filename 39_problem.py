#Create a random 5 × 3 matrix and a random 3 × 2 matrix containing integers from 1 to 9. Then perform the real matrix product (matrix multiplication) and store the result in a new matrix.

import numpy as np
A = np.random.randint(1,10,(5,3))
B = np.random.randint(1,10,(3,2))

c = A @ B
print("Matrix A:\n",A)
print("Matrix B:\n",B)
print("Result (A x B):\n",c)