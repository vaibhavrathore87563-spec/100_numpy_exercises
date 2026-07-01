#Given the following image array, find the unique RGB colors and count how many unique colors are present in the image.

import numpy as np
img = np.array([
                [[1,2,3],[4,5,6]],
                [[1,2,3],[4,5,6]]
],dtype =np.uint8)

colors = np.unique(img.reshape(-1,3), axis=0)
print(colors)

print(len(colors))