# strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
# integer - used to represent integer numbers. e.g. -1, -2, -3
# float - used to represent real numbers. e.g. 1.2, 42.42
# boolean - used to represent True or False.
# complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j

# Data Types in NumPy

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

# ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.

# Checking the Data Type of an Array

import numpy as np

arr = np.array([1,2,3,4,5])

print(arr.dtype)

print('~' * 120)

################################################################################3

import numpy as np

arr = np.array(['hai', 'bye', 'tata'])

print(arr.dtype)

print('~' * 120)

################################################################################

import numpy as np

arr = np.array([1,2,3,4,5], dtype='S')

print(arr)

print(arr.dtype)

print('~' * 120)

################################################################################

import numpy as np

arr = np.array([1,2,3,4,5], dtype='i4')

print(arr)

print(arr.dtype)

print('~' * 120)

################################################################################

# import numpy as np

# arr = np.array(['a', '2', '3'], dtype='i')

# print(arr)

# print(arr.dtype)

print('~' * 120)

################################################################################

# Converting Data Type on Existing Arrays

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

print('~' * 120)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)

################################################################################






