#Create a custom NumPy dtype named employee to store employee information with the following fields:

#id → int32
#age → int32
#salary → float32

import numpy as np
employee = np.dtype([
           ('id', np.int32),
           ('age', np.int32),
           ('salary', np.float32)
])
print(employee)

