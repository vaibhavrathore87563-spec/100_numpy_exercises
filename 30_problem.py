#Create a 5×5 diagonal matrix with random integers between 1 and 20 on the main diagonal using NumPy.

import numpy as np
arr = np.diag(np.random.randint(1,21,5))
print(arr)