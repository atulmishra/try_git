# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 14:49:32 2018

@author: Administrator
"""
import numpy as np 
import pandas as pd
np.set_printoptions(threshold=np.inf)

df = pd.read_csv('Data.csv')

#df = pd.DataFrame({"Age":age, "Salary":salary})
def Normalization(data):
    nmin = np.min(data)
    nmax = np.max(data)
    if(nmax == nmin):
        return None
    normalize = nmax - nmin
    return [float(e-nmin)/normalize for e in data]

data = df["Salary"]
print (Normalization(data))

from sklearn import preprocessing
x = df.values
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)

df = pd.DataFrame(x_scaled)

print(df)
