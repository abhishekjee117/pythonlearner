'''
NDARRAY OBJECT
'''
# ndarray : N-dimensional array
# Each element in an ndarray is an object of type "dtype" (data-type object)
# Syntax:
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

import numpy as np

print("This is a 1-D array!")
a = np.array([1,2,3])
print(a)

print("This is a 2-D array!")
a = np.array([[1,2],[3,4]])
print(a)

print("Minimum dimensions in an array!")
a = np.array([1,2,3,4,5], ndmin = 2)
print(a)

print("Printing elements as of dtype complex")
a = np.array([1,2,3], dtype = complex)
b = np.array([[1,2],[3,4]], dtype = complex)
print(a)
print(b)
