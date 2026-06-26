 #Create a checkerboard 8x8 matrix using the tile function


import numpy as np
arr = np.tile([[1,0]
               ,[0,1]],(4,4))
print(arr)
# np.tile(array, (rows_repeat, columns_repeat))