#Insert a Space Between Characters

import numpy as np
arr = np.array(['Hello', 'Numpy'])
result = [' ' .join(word) for word in arr]
print(result)



import numpy as np
arr = np.array(['hy','mr','vaibhav']) 
result = [' '.join(word)for word in arr]
print(result)