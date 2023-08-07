# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 22:12:12 2023

@author: abhishek.jee
"""

# ---PANDAS DATAFRAME---

import pandas as pd
import numpy as np

'''
    Pandas dataframes are 2-D homogenous arrays that are labeled, size-mutable and value-mutable.

    They are created using a DataFrame constructor, the syntax of which is as follows:
        pandas.DataFrame(data, index, columns, dtype, copy)
        
    A dataframe can be created using various inputs such as:
        List
        Dict
        Numpy ndarray
        Series
        Another DataFrame
'''

# ---CREATING AN EMPTY DATAFRAME---

print("\nCreating an empty dataframe...")
df = pd.DataFrame()
print("The dataframe \"df\" is:")
print(df)
print("The type of the dataframe \"df\" is:")
print(type(df))
print("\n")

# ---CREATING A DATAFRAME FROM LISTS---

print("\nCreating a dataframe from lists...")
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)
print("As you can see, since there was no column defined for the series data, a default value of \"0\" is associated with the column as the column-name!")

print("\nCreating a 2-D dataframe with column names...")
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)

print("\nCreating a 2-D dataframe with column names and declaring a datatype...")
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)

# ---CREATING A DATAFRAME FROM DICTIONARY OF NDARRAY/LISTS---

print("\nCreating a 2-D dataframe from a dictionary of lists...")
data = {'Name':['Tom','Jack','Steve','Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)
print("In the above dataframe, the keys are considered as the column names, and their respective values as the columns' values. The individual key:value pairs may be visualized as individual series that are contained within the dataframe!")

# ---CREATING A DATAFRAME FROM A LIST OF DICTIONARIES---

print("\nCreating a 2-D dataframe from a list of dictionaries...")
data = [{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df = pd.DataFrame(data)
print(df)
print("Why is column \"c\" housing float values while columns a and b have int values?")

print("\nCreating a 2-D dataframe from a list of dictionaries and using row indices...")
data = [{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df = pd.DataFrame(data,index=['first','second'])
print(df)

print("\nCreating a 2-D dataframe from a list of dictionaries and using row indices AND column indices...")
data = [{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df1 = pd.DataFrame(data,index=['first','second'],columns=['a','b'])
df2 = pd.DataFrame(data,index=['first','second'],columns=['a','b1'])
print(df1)
print(df2)
print("In the dataframe \"df2\", since the second column was named \"b1\", and there is actually no key:value pair that has \"b1\" as its key, the column is generated with having null values in it!")
print("\n")

# ---CREATING A DATAFRAME FROM A DICTIONARY OF SERIES---

print("\nCreating a 2-D dataframe from a dictionary of series...")
d = {
     'one':pd.Series([1,2,3],index=['a','b','c']),
     'two':pd.Series([1,2,3,4],index=['a','b','c','d'])
     }
df = pd.DataFrame(d)
print(df)
print("When we combine two different series in a single dataframe, their indexes are unionised!")
print("\n")

# ---COLUMN SELECTION---

print("\nPerforming a column selection...")
d = {
     'one':pd.Series([1,2,3],index=['a','b','c']),
     'two':pd.Series([1,2,3,4],index=['a','b','c','d'])
     }
df = pd.DataFrame(d)
print(df)
print("The column with header \"one\" is:")
print(df['one'])
print("The column with header \"two\" is:")
print(df['two'])
print("\n")

# ---COLUMN ADDITION---

print("\nPerforming a column addition...")
d = {
     'one':pd.Series([1,2,3],index=['a','b','c']),
     'two':pd.Series([1,2,3,4],index=['a','b','c','d'])
     }
df = pd.DataFrame(d)
print(df)
print("Adding a new column...")
df['three']=pd.Series([10,20,30],index=['a','b','c'])   # adding a new series along with index
print("The modified dataframe is now:")
print(df)
print("Adding another new column...")
df['four'] = df['one'] + df['three']        # simply adding the corresponding elements of two columns
print("The modified dataframe is now:")
print(df)
print("\n")

# ---COLUMN DELETION---

print("\nPerforming a column deletion...")
d = {
     'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
     'three' : pd.Series([10,20,30], index=['a','b','c'])
     }
df = pd.DataFrame(d)
print("Our dataframe is:")
print(df)
print("Deleting a column form the dataframe \"df\"...")
del df['one']
print("The modified dataframe is now:")
print(df)
print("Deleting another column using the \"pop()\" function...")
df.pop('two')
print("The modified dataframe is now:")
print(df)
print("The \"del\" operator is used when the dataframe columns are being addressed in a list manner.")
print("The \"pop()\" function is used otherwise.")
print("The \"del\" operator simply deletes the column, while the \"pop()\" function deletes the column and also returns the popped column!")
print("\n")

# ---ROW SELECTION/ADDITION/DELETION---

print("\nPerforming a row selection by label...")
d = {
     'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
     'three' : pd.Series([10,20,30], index=['a','b','c'])
     }
df = pd.DataFrame(d)
print(df.loc['b'])
print("\nPerforming a row selection by integer location...")
print(df.iloc[2])
print("\n")

# ------


# ------