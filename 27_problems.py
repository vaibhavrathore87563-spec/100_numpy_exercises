#create a 4×4 diagonal matrix with negative values [-1, -2, -3, -4] on the main diagonal.

import numpy as np
arr = np.diag((-1,-2,-3,-4),k=0)

print(arr)
