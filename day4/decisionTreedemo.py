# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 10:16:02 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("accident.csv")

X = dataset.iloc[:,0:8].values
y=  dataset.iloc[:,len(dataset.iloc[0])-1].values


from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X,y)

y_pred_TX_Drunk =  regressor.predict([[48,6,2,2,1,2,4,1]])
print("Drunk Driver", y_pred_TX_Drunk)

y_pred_TX_Sober =  regressor.predict([[48,6,2,2,1,2,4,0]])
print("No Drunk Driver", y_pred_TX_Sober)

from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz 
import pydotplus
from sklearn import tree

dot_data = tree.export_graphviz(regressor)

from mpl_toolkits.mplot3d import axes3d
