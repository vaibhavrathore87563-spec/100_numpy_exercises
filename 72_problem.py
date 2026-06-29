#Create a NumPy array containing 500 random integers between 1 and 99 and print all the elements without truncating the output.

import numpy as np
arr = np.random.randint(1,100,500)
np.set_printoptions(threshold=np.inf)
arr = print(arr)