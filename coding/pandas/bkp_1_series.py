# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 18:16:07 2023

@author: abhishek.jee
"""

import pandas as pd
import numpy as np


# ---DATA STRUCTURES---

# Series    : 1-D, labeled, size-immutable, homogenous, value-mutable
# DataFrame : 2-D, labeled, size-mutable, heterogenous, value-mutable
# Panel     : 3-D, labeled, size-mutable, heterogenous, value-mutable

# ---SERIES---

'''
    Syntax:
        pandas.Series(data, index, dtype, copy)
'''

'''
    A series can be created using:
        Array
        Dictionary
        Scalar value or constant
'''

s = pd.Series()
print(s)

# Creating a series form an ndarray without an index

print("\nCreating a series form an ndarray without an index...")
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(data)
print(s)
print("The data type of the numpy array \"data\" is:",type(data))
print("The data type of the series \"s\" is:",type(s))

# Creating a series form an ndarray with a custom index

print("\nCreating a series form an ndarray with a custom index...")
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print(s)

# Creating a series from a dictionary without an index

print("\nCreating a series from a dictionary...")
data = {'a':0,'b':1,'c':2}
s = pd.Series(data)
print(data)
print(s)

# Creating a series from a dictionary with a custom index

print("\nCreating a series form a dictionary with a custom index...")
data = {'a':0,'b':1,'c':2}
s = pd.Series(data,index=['b','c','d','a'])
print(s)
print("As you can see, the index order remains just as it was declared/defined in the original dictionary!")

# Creating a series from a scalar
# A scalar value is a one-dimensional value
# A vector value is a two-dimensional or three-dimensional value

print("\nCreating a series from a scalar...")
s = pd.Series(5,index=[0,1,2,3])
print(s)
print("As you can see, the data value is repeated for as many indexes there are!")

# Accessing data from series with position

print("\nAccessing data from series with position...")
s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print("The first element stored in the series is:",s[0])
print("The first 3 elements stored in the series are:\n")
print(s[:3])
print("The last 3 elements stored in the series are:\n")
print(s[-3:])

# Retrieving data using a label/index

print("\n# Retrieving data using a label/index...")
s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print("Retrieving a single element:")
print(s['a'])
print("Retrieving multiple elements:")
print(s[['a','c','d']])
print("Retrieving an element that is not there:...this will throw an exception...")
# print(s['f'])

