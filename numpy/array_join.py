# Joining NumPy Arrays
# Joining means putting contents of two or more arrays in a single array.
# In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
# We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

import numpy as np

# Join two arrays
arr1 = np.array([1,2,3])
arr2 = np.array([6,7,8,])
arr = np.concatenate((arr1,arr2))
print(arr)

# Join two 2-D arrays along rows (axis=1):
arr3 = np.array([[1,2],[3,4]])
arr4 = np.array([[5,6],[7,8]])
arr_1 = np.concatenate((arr3,arr4), axis=1)
print(arr_1)

# # Joining Arrays Using Stack Functions
# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
# We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
# We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.
arr5 = np.array([1,2,3])
arr6 = np.array([4,5,6])
arr_2 = np.stack((arr5, arr6), axis=1)
print(arr_2)

# Stacking Along Rows
# NumPy provides a helper function: hstack() to stack along rows.
arr7 = np.array([1, 2, 3])
arr8 = np.array([4, 5, 6])
arr_3 = np.hstack((arr7, arr8))
print(arr_3)

# Stacking Along Columns
# NumPy provides a helper function: vstack()  to stack along columns.
arr9 = np.array([1, 2, 3])
arr10 = np.array([4, 5, 6])
arr_4 = np.vstack((arr9, arr10))
print(arr_4)

# Stacking Along Height (depth)
# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
arr11 = np.array([1, 2, 3])
arr12 = np.array([4, 5, 6])
arr_5 = np.dstack((arr11, arr12))
print(arr_5)