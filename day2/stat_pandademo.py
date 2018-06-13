# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 13:45:56 2018

@author: Administrator
"""


import numpy as np
import pandas as pd
import statistics

df = pd.read_csv("diabetes.csv")

#print("Dataframe", df)


#print(df['BMI'])

a= df['BMI']
print("BMI")

print("median")

print (statistics.stdev(a))
print (statistics.stdev(a))