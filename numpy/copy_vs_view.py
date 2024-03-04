# The copy SHOULD NOT be affected by the changes made to the original array.

import numpy as np

arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
print('~' * 120)
################################################################################################

# The view SHOULD be affected by the changes made to the original array.
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)