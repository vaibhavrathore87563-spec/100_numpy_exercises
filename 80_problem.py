import numpy as np
n = 10 #array size
p = 5 # number of element to place

arr = np.zeros((n,n))
x = np.random.choice(n*n, p, replace= False)
arr.flat[x] = 1

print(arr)
# np.random.choice(n*n , p) --> choose random position in n*n array
# p is the (number of elements to place) in this n*n array
# replace=False ensures no position is selected twice.
# flat() --> treats the 2D array as a 1D sequence.