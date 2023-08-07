# ---PYTHON NUMPY - NDARRAY---

import numpy as np

'''
    ndarray :   An n-dimensional array comprising of contiguous 1-dimensional memory segments of the same size, with an indexing scheme that maps each item to a location in the memory block.
    Syntax for creating an ndarray object
        numpy.array(object, dtype, copy, order, subok, ndmin)
    where
        object  :   Any object exposing the array interface method returns an array, or any (nested) sequence.
        dtype   :   Desired data type of array, optional
        copy    :   Optional. By default (true), the object is copied
        order   :   C (row major) or F (column major) or A (any) (default)
        subok   :   By default, returned array forced to be a base class array. If true, sub-classes passed through
        ndmin   :   Specifies minimum dimensions of resultant array
'''

# ---CREATING A BASIC NDARRAY---

print("\nCreating a basic ndarray...")
a = np.array([1,2,3])
print("The array \"a\" is :")
print(a)
print("The type of the array \"a\" is:")
print(type(a))
print("\nA normal list \"[1,2,3]\" is printed as-is, but when it's converted to an ndarray, it is printed as \"[1 2 3]\"!")
print("\n")

print("\nCreating a basic 2-D ndarray...")
a = np.array([[1,2],[3,4]])
print("The original data is:")
print([[1,2],[3,4]])
print("The array \"a\" around the original data is:")
print(a)
print("\n")

# ---CREATING A NDARRAY WITH MINIMUM DIMENSIONS---

print("\nCreating an ndarray with minimum dimensions...")
lst = [1,2,3,4,5]
a = np.array(lst, ndmin=2)
print("The original list variable is:")
print(lst)
print("The ndarray around that list is:")
print(a)
print("\n")

# ---CREATING A NDARRAY WITH A DTYPE PARAMETER---

print("\nCreating an ndarray with a dtype parameter...")
lst = [1,2,3]
a = np.array(lst, dtype=complex)
print(a)
print("\n")
