import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
arr = np.random.randint(1,10, (8,8))
print(arr)
blocks = sliding_window_view (arr, (3,3))
print(blocks.shape)