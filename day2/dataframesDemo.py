# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 12:30:34 2018

@author: Administrator
"""


import pandas as pd

df1 = pd.read_csv("https://www.quandl.com/api/v3/datasets/WIKI/AAPL.csv")
df = pd.read_csv("Data.csv")
print("Dataframe", df)
print("Dataframe1", df1)


print("Shape", df.shape)
print("Length", len(df))
print("Column Headers",df.columns )
print("Data Types", df.dtypes)
print("Index", df.index)
print("Values", df.values)

print(df.head(2))
print(df.tail(2))

print(df['Age'])
print(df[0:3])
print("Loc")

print(df.loc[[0,8],:])
print(df.iloc[:,0])
print(df.iloc[:,0:2])
print("iLoc")

print(df.iloc[[0,3,6],[0,2]])



