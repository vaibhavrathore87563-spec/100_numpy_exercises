#Considering 2 vectors A & B, write the einsum equivalent of inner, outer, sum, and mul function (★★★)

import numpy as np
A = np.array([1,2,3])
B = np.array([4,5,6])

print("Vector A:" ,A)
print("Vector B:",B)

# 1. Inner Product

print("\n1. Inner Product")

print("Using np.inner():")
print(np.inner(A , B))

print("Using einsum():")
print(np.einsum('i,i->' , A ,B))


# 2. Outer Product
print("\n2. Outer product")

print("using np.outer():")
print("np.einsum ():")
print(np.einsum('i , j->ij',A , B))