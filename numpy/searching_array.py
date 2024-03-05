# NumPy Searching Arrays
# You can search an array for a certain value, and return the indexes that get a match.
# To search an array, use the where() method.
# The example above will return a tuple: (array([3, 5, 6],)
# Which means that the value 4 is present at index 3, 5, and 6.
# Only called index

import numpy as np

arr = np.array([1,2,3,4,7,4,4])

# where
print(np.where(arr == 4))
print(np.where(arr%2 == 0))

# Search Sorted
# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
arr1 = np.array([6, 7, 8, 9])
x = np.searchsorted(arr1, 7)
print(x)

# search sorted right
arr2 = np.array([6, 7, 8, 9])
y = np.searchsorted(arr2, 7, side='right')
print(y)

# Multiple Values
arr3 = np.array([1, 3, 5, 7])
z = np.searchsorted(arr3, [2, 4, 6])
print(z)