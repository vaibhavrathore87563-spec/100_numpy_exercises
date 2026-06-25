#Create a 5×5 matrix whose diagonal elements are the squares of numbers 1 to 5

import numpy as np
arr = np.diag(np.arange(1,6) **2)
print (arr)