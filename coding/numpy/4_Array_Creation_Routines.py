# ---NUMPY - ARRAY CREATION ROUTINES---

import numpy as np

'''
    A new ndarray can be constructed using any of the following array creation routines or using a low-level ndarray constructor.
        numpy.empty : it creates an uninitialized array of specified shape and dtype. It uses the following constructor:
            numpy.empty(shape, dtype = float, order = 'C')
            where,
                1	:	Shape	:	Shape of an empty array in int or tuple of int.
                2	:	Dtype	:	Desired output data type. Optional.
                3	:	Order	:	'C' for C-style row-major array, 'F' for FORTRAN style column-major array.
        numpy.zeros : 
        numpy.ones  : 
    
'''

# ---numpy.empty()---

print("\n...")
x = np.empty([3,2], dtype = int)
print(x)
print("The elements in the uninitialized array show random values as they are not initialized.")
print("\n")

