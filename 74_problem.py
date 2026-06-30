#Find the closest value to 67 in the array below.

import numpy as np
arr = np.array([12,25,48,70,95])
value = 67

Distance = arr - value
sign_rmv = np.abs (Distance)
closet_value = arr [(sign_rmv.argmin())]

print(Distance)
print(closet_value)
print(sign_rmv)