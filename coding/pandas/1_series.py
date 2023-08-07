# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 21:04:25 2023

@author: abhishek.jee
"""

# ---PANDAS SERIES---

import pandas as pd
import numpy as np

'''
    Pandas series are 1-D homogenous arrays that are labeled, size-immutable and value-mutable.

    They are created using a Series constructor, the syntax of which is as follows:
        pandas.Series(data, index, dtype, copy)
        
        data    It takes various forms like ndarray, list, constants.
        index   The values must be unique and hashable, same length as data. Default np.arrange(n) if no index is passed.
        dtype   It is for data type. If None, data type will be inferred.
        copy    It is to copy data. Default False.
        
    A series can be created using various inputs such as:
        Array
        Dict
        Scalar value or constant
'''

# ---CREATING AN EMPTY SERIES---

print("\nCreating an empty series...")
s = pd.Series()
print("The empty series is:")
print(s)
print("The type of the empty series is:")
print(type(s))
print("\n")

# ---CREATING A SERIES FROM NDARRAY---

print("\nCreating a series from an ndarray...")
data = np.array(['a','b','c','d','e'])
s = pd.Series(data)     # no index has been defined for this series
print("The numpy array \"data\" is:")
print(data)
print("The type of the numpy array \"data\" is:",type(data))
print("The series \"s\" built around \"data\" array is:")
print(s)
print("The type of the series \"s\" is:",type(s))
print("\n")

print("\nCreating a series from an ndarray, using a customized index...")
data = np.array(['a','b','c','d'])
s = pd.Series(data, index=[100,101,102,103])
print(s)
print("\n")

# ---CREATING A SERIES FROM A DICTIONARY---

print("\nCreating a series from a dictionary...")
data = {'a':0,'b':1,'c':2}
s = pd.Series(data,index=['b','c','d','a'])
s_i = pd.Series(data)
print("The dictionary \"data\" is:")
print(data)
print("The series \"s\" derived from the dictionary is:")
print(s)
print("In the above series, the index order is maintained as it was in the original dictionary. The index that has no associated element gets a \"NaN\" associated with itself!")
print("The series \"s_i\", but without index, is:")
print(s_i)
print("In the above series, the dictionary keys themselves are used to construct the index for the series!")
print("\n")

# ---CREATING A SERIES FROM A SCALAR---

print("\nCreating a series from a scalar...")
s = pd.Series(5,index=[0,1,2,3])
print(s)
print("In the above series, the data assigned to the series is a scalar, and therefore, the index HAS to be provided. The value will be repeated so many times as to match the length of the index!")
print("\n")

# ---ACCESSING DATA IN A SERIES USING POSITION---

print("\nAccessing data in a series using position...")
s = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(s)        # prints the entire series
print(s[0])     # prints the first element of the series
print(s[:3])    # prints the first 3 elements of the series, i.e. from 0 to 2
print(s[-3:])   # prints the last 3 elements of the series
print("\n")

# ---RETRIEVING DATA USING LABEL(INDEX)---

print("\nRetrieving data from a series using label(index)...")
s = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(s['a'])           # prints the element located at index 'a'
print(s[['a','c','d']]) # prints the elements located at indices 'a', 'c' and 'd'
#print(s['f'])           # prints the elements located at index 'f', which itself does not exist. Hence, this will result in an error   -->     KeyError: 'f'