# ---PYTHON NUMPY - ARRAY STTRIBUTES---

import numpy as np

'''
    Array attributes in NumPy:
        ndarray.shape       : returns a tuple consisting of the array's dimensions.
        ndarray.reshape()   : reshapes a given array in the format provided as arguments to the function.
        ndarray.ndim        : returns the number of array dimensions.
        numpy.itemsize      : returns the length of each element of the array in bytes.
        numpy.flags
            1	:	C_CONTIGUOUS (C)	:	The data is in a single, C-style contiguous segment
            2	:	F_CONTIGUOUS (F)	:	The data is in a single, Fortran-style contiguous segment
            3	:	OWNDATA (O)			:	The array owns the memory it uses or borrows it from another object
            4	:	WRITEABLE (W)		:	The data area can be written to. Setting this to False locks the data, making it read-only
            5	:	ALIGNED (A)			:	The data and all elements are aligned appropriately for the hardware
            6	:	UPDATEIFCOPY (U)	:	This array is a copy of some other array. When this array is deallocated, the base array will be updated with the contents of this array
        
'''

# ---ndarray.shape---

print("\nndarray.shape...")
a = np.array([[1,2,3],[4,5,6]])
print("The dimensions of the ndarray \"a\" in (row,column) format are:",a.shape)
print("\n")

print("Resizing an ndarray...")
a = np.array([[1,2,3],[4,5,6]])
print("The original ndarray is:")
print(a)
a.shape = (3,2)
print("After resizing, the ndarray is now:")
print(a)
print("As you can see, the rows have been changed to columns and vice versa!")
print("\n")

# ---ndarray.reshape()---

print("\nResizing an ndarray using the reshape() function...")
a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print("The original array \"a\" is:")
print(a)
print("The array \"b\" from reshaping array \"a\" is")
print(b)
print("\n")

# ---ndarray.ndim---

print("\nUsing the arange() function to construct an array...")
a = np.arange(24)
print(a)
print(a.shape)
print(a.ndim)   # prints the number of dimensions of the array "a"
print("\n")

b = a.reshape(2,4,3)    # reshape(2,4,3) will arrange the contents of the array into 2 parts, where each part would consist of 4 rows and 3 columns
print(b)
print(b.ndim)

# ---numpy.itemsize---

print("\n...")
x = np.array([1,2,3,4,5], dtype = np.int8)
print(x.itemsize)
y = np.array([1,2,3,4,5], dtype = np.float32)
print(y.itemsize)
print("\n")

# ---numpy.flags---

print("\n...")
x = np.array([1,2,3,4,5])
print(x.flags)
print("\n")
