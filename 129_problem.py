#(Python)
#copy vs view ()
nums = [1,2,3,4,5,6]
sub_list = nums[1:3]
print(sub_list)
sub_list[0]=300
print(sub_list)
print(nums)


#numpy
#slicing in numpy does not create a copy create a view
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
sub_arr = arr[1:3]
print(sub_arr)
sub_arr[0]=123
print(sub_arr)
print(arr)