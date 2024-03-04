import numpy as np

arr1 = np.array([[1,2],[7,8]])
arr2 = np.array([[4,5], [11,12]])

arr = np.concatenate((arr1,arr2), axis=1)
print(arr)