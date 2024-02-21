# Slicing in python means taking elements from one given index to another given index.
# Note: The result includes the start index, but excludes the end index.

import numpy as np

arr = np.array([1,2,3,4,5,6,7])

print(arr[1:5])
print(arr[4:])
print(arr[:5])
print(arr[-3:-1]) # Negative Slicing
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# STEP
import numpy as np

arr = np.array([1,2,3,4,5,6,7])

print(arr[0:5:2])
print(arr[::2])
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Slicing 2-D Arrays
# Note: Remember that second element has index 1.

import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arr[1, 1:4])
print(arr[0:2, 2])
print(arr[0:2, 1:4]) # [1,2,3,4,5] ==> 0 | [6,7,8,9,10] ==> 1 | [] ==> 2

# Note:
# slicing 2-D array va protha varaikum arr[:] ==> left side kodukura value 0,1,2 va consider pannum and right side kodukura value slicing pannum
