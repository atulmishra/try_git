# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:55:57 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:27:05 2017

@author: BALASUBRAMANIAM
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
from sklearn.datasets import load_boston
boston=load_boston()

print(boston.keys())



print(boston.data.shape)

print(boston.data)


print(boston.feature_names)

print(boston.DESCR)

bos=pd.DataFrame(boston.data)
#default head takes row=5
#print(bos.head())

#modify column names
bos.columns=boston.feature_names
print(bos.head(10))
print(boston.target)

#housing prices are in target
print(boston.target[0:5])
#add price in data frame
bos['PRICE']=boston.target
print(bos.head())
'''
#fit linear regression model to find housing price
Y = boston housing price(also called “target” data in Python)

and

X = all the other features (or independent variables)
'''

from sklearn.linear_model import LinearRegression
X=bos.drop(['PRICE','NOX'],axis=1)

#X=bos.RM
lm=LinearRegression()
lm.fit(X,bos.PRICE)
LinearRegression(copy_X=True, fit_intercept=True, normalize=False)
print("Estimated intercept coefficient",lm.intercept_)
print("Number of coefficients",len(lm.coef_))

plt.scatter(bos.RM,bos.PRICE)
plt.xlabel("Average Rooms per Dwelling RM")
plt.ylabel("Housing Price")
plt.title("Relationship between RM and Price")
plt.show()

#predicting price
print(lm.predict(X)[0:5])
plt.scatter(bos.RM,lm.predict(X))
plt.plot(bos.RM,lm.predict(X), 'm.') #color code is k or m or etc.,
plt.xlabel("Prices")
plt.ylabel("Predicted Price")
plt.title("Price vs Predicted Price")
plt.show()



#Mean Squared Error
MSE=np.mean((bos.PRICE-lm.predict(X))**2)
print("Mean Squared Error %r" %(MSE))
#Sum of Sqaured Error
SSE=np.sum((bos.PRICE-lm.predict(X))**2)
print("SUM of Sqaured Error %r" %(SSE))

