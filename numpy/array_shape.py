# Shape of an Array
# The shape of an array is the number of elements in each dimension.

import numpy as np

arr = np.array([[1,2,3,4], [5,6,7,8]])

print(arr.shape)

print('~' * 120)

################################################################################

import numpy as np

arr = np.array([1,2,3,4,5], ndmin=5)

print("shape of an array : ", arr.shape)