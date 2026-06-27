import numpy as np
np.seterr(divide = 'ignore')

a = np.array([2,0,5])
print(10/a)

#practice question
#Without executing the code, predict the output and explain why NumPy does not display an overflow warning.

import numpy as np
np.seterr(over = 'ignore')

a = np.array([1e308, 2e308 , 3.0])
print(a *10)