# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:50:26 2018

@author: Administrator
"""

from sklearn.metrics import confusion_matrix


expected = [1,1,0,1,0,0,1,0,0,0]
predicted =[1,0,0,1,0,0,1,1,1,0]

results = confusion_matrix(expected, predicted)

print(results)