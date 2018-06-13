# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 15:45:29 2018

@author: Administrator
"""
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Position_Salaries.csv")

X= dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree =4)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
lin_reg_2 =LinearRegression()
lin_reg_2.fit(X_poly, y)


plt.scatter(X,y,color = 'red')
plt.plot(X,lin_reg.predict(X), color='blue') #color code is k or m or etc.,
plt.title("Truth vs Bluff(Linear Regression) ")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.show()



plt.scatter(X,y,color = 'red')
plt.plot(X,lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue') #color code is k or m or etc.,
plt.title("Truth vs Bluff (Polynomial Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()


#X_grid = np.arange(min(X), max(X))