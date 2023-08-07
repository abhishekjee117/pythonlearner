# -*- coding: utf-8 -*-
"""
Created on Tue May  2 01:04:52 2023

@author: Owner
"""

# ---PYTHON NUMPY - DATA TYPES---

import numpy as np

'''
    Scalar data types defined in NumPy:
        1   :	bool_		:	Boolean (True or False) stored as a byte
        2   :	int_		:	Default integer type (same as C long; normally either int64 or int32)
        3   :	intc		:	Identical to C int (normally int32 or int64)
        4   :	intp		:	Integer used for indexing (same as C ssize_t; normally either int32 or int64)
        5   :	int8		:	Byte (-128 to 127)
        6   :	int16		:	Integer (-32768 to 32767)
        7   :	int32		:	Integer (-2147483648 to 2147483647)
        8   :	int64		:	Integer (-9223372036854775808 to 9223372036854775807)
        9   :	uint8		:	Unsigned integer (0 to 255)
        10  :	uint16		:	Unsigned integer (0 to 65535)
        11  :	uint32		:	Unsigned integer (0 to 4294967295)
        12  :	uint64		:	Unsigned integer (0 to 18446744073709551615)
        13  :	float_		:	Shorthand for float64
        14  :	float16		:	Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
        15  :	float32		:	Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
        16  :	float64		:	Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
        17  :	complex_	:	Shorthand for complex128
        18  :	complex64	:	Complex number, represented by two 32-bit floats (real and imaginary components)
        19  :	complex128	:	Complex number, represented by two 64-bit floats (real and imaginary components)
'''

'''
    A dtype object is constructed using the following syntax:
        numpy.dtype(object, align, copy)
    where
        object  − To be converted to data type object
        align   − If true, adds padding to the field to make it similar to C-struct
        copy    − Makes a new copy of dtype object. If false, the result is reference to builtin data type object
'''

# ---USING AN ARRAY SCALAR TYPE---

print("\nUsing an array scalar type...")
dt = np.dtype(np.int32)
print(dt)
print("\n")

# ---#---

print("\n...")
print("\n")

# ---#---

print("\n...")
print("\n")

# ---#---

print("\n...")
print("\n")

# ---#---

print("\n...")
print("\n")

# ---#---