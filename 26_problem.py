#Create a 7×7 diagonal matrix with values 2, 4, 6, 8, 10, 12, 14 on the main diagonal.

import numpy as np
arr = np.zeros((7,7),dtype = int)
np.fill_diagonal(arr,[2,4,6,8,10,12,14])

print(arr)