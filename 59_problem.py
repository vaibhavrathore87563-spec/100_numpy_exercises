
#Create a random vector of size 15 containing numbers from 50 to 100 and sort it in ascending order.
import numpy as np
arr = np.random.randint(50,101,15)


print("Original Array:",arr)
print("Sorted Array:",np.sort(arr))
