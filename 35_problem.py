#Using only np.tile(), create a 10 × 10 chessboard pattern starting with 0 in the top-left corner.

import numpy as np
arr = np.tile([[0,1],
                [1,0]],(5,5))
print(arr)