import numpy as np
arr = np.diag(np.arange(1,6) **3)
print(arr)
print("Digonal Maximum value =",np.max(arr))