import numpy as np

arr = np.diag((1,2,3,4,5),k = 0) 
print(arr)

# k=0	Main diagonal
# k=1	First diagonal above the main diagonal
# k=2	Second diagonal above the main diagonal
# k=-1	First diagonal below the main diagonal
# k=-2	Second diagonal below the main diagonal

#Create a 4×4 diagonal matrix with values 10, 20, 30, and 40 on the main diagonal.

import numpy as np
arr = np.diag((10,20,30,40),k=0)
print(arr)