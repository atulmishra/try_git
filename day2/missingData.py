# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 14:03:21 2018

@author: Administrator
"""

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
np.set_printoptions(threshold=np.inf)

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values#rxclude last
#print("X")
#print("temp")
#print(dataset.iloc[:,1:3].values)#rxclude last

#print(X)

Y = dataset.iloc[:, 3].values
print("Y")

print(Y)
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy = 'mean', axis =0)

imputer = imputer.fit(X[:,1:3])
#print(imputer)
X[:,1:3] = imputer.transform(X[:,1:3])

#print(X)


from sklearn.preprocessing import LabelEncoder
labelencoder_X =LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
#print (X)

labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)
print(Y)


