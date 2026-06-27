# Create a vector of size 10 with values ranging from 1 to 100, both included

import numpy as np
arr = np.linspace(1,1000,12)
print("value between 1 to 1000",arr)



#Create a vector of size 18 with values ranging from 25 to 250, both excluded.

import numpy as np
arr = np.linspace(25,250,20)[1:-1]
print("value between 25 to 250",arr)
