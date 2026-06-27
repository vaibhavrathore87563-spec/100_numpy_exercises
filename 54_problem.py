#create a generator function that yields the squares of numbers from 0 to 4 and use it to build a NumPy array.

import numpy as np

def square():
    for i in range(5):
        yield i**2

arr = np.fromiter(square(), dtype = int)

print(arr)

#Write a generator that generates the first five perfect cube and convert it into a NumPy array using np.fromiter().

import numpy as np
def cube():
 for i in range(1,6):
   yield i**3

   arr = np.fromiter(cube(), dtype = int)

   print(arr)