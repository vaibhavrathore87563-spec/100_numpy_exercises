# How to get the diagonal of a dot product?

import numpy as np
A = np.arange(9).reshape(3,3)
B = np.arange(9).reshape(3,3)

print("Array One:\n",A)
print("Array Two:\n",B)

c = np.dot(A , B)
print("A x B\n",c)
D = np.diag(c)
print("Diagonal : ",D)