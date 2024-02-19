# Array indexing is the same as accessing an array element.

import numpy as np

arr = np.array([1,2,3,4,5])

# Get the first element from the following array:
print(arr[0])
# Get the second element from the following array.
print(arr[1])
# Get third and fourth elements from the following array and add them.
print(arr[2] + arr[3])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``

# Access 2-D Arrays

import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
print(arr.ndim)
print("2nd element is 1st row : ", arr[0,1])
print('4th lement in 1st row: ', arr[0,4])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``

# Access 3-D Arrays
import numpy as np

arr = np.array([[[1,2,3],[5,6,7]],[[8,9,10],[11,12,13]]])

# Access the third element of the second array of the first array:
print(arr[0,1,2])

# `~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Negative Indexing
import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# Print the last element from the 2nd dim:
print("Last element from 2nd dimension: ", arr[1,-1])