# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:17:17 2018

@author: Administrator
"""

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

import sklearn

from sklearn.datasets import load_boston
boston = load_boston()

print(boston.keys())

print (boston.data.shape)

print(boston.data)

print(boston.feature_names)

print(boston.DESCR)

print(boston.target)

bos= pd.DataFrame(boston.data)
bos.columns=boston.feature_names
print("bos head")
print(bos.head)

print(boston.target[0:5])

bos["PRICE"] = boston.target


from sklearn.linear_model import LinearRegression

X=bos.drop(['PRICE','NOX'],axis=1)

#X=bos.RM
lm=LinearRegression()
lm.fit(X,bos.PRICE)
LinearRegression(copy_X=True,fit_intercept=True, normalize=False)
print("Estimated intercept coefficient", lm.intercept_)
print("Number of coefficients", len(lm.coef_))

plt.scatter(bos.RM, bos.PRICE)
plt.title('Relationship between RM and Price')
plt.xlabel('Average Rooms per Dwelling RM')
plt.ylabel('House Price')
plt.show()

print(lm.predict(X)[0:5])
plt.scatter(bos.RM,lm.predict(X))
plt.plot(bos.RM,lm.predict(X), 'k.')
plt.title('Price vs Predicted Price')
plt.xlabel('Prices')
plt.ylabel('Predicted Prices')
plt.show()


#Mean Sqaured Error
MSE=np.mean((bos.PRICE-lm.predict(X))**2)
print("Mean Sqaured Error %r" %(MSE))
#Sum of Sqaured Error
SSE=np.sum((bos.PRICE-lm.predict(X))**2)
print("SUM of Sqaured Error %r" %(SSE))