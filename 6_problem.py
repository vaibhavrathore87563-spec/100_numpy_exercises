#How to find a memory size of any array
import numpy as np

arr = np.array([[[1,3],[4,5],[6,7],[8,9]]])
print("Memory Size=" , arr.nbytes)
print(arr.size)
#each value take a 8 bytes to take a memory
