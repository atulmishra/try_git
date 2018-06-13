# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 12:29:22 2018

@author: Administrator
"""
import matplotlib.pyplot as plt
import numpy as np

x =[[6],[8],[10],[14],[18]]
print(x[0])
y = [[7], [9] , [13], [17.5],[18]]


plt.figure()
plt.title('Pizza price plotted against diameter')
plt.xlabel('Diameter in inches')
plt.plot(x,y,'m.')
plt.axis([0,25,0,25])
plt.grid(True)
plt.show()

from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(x,y)
print('A 13" pizza should cost: $%.2f ' %model.predict(13)[0])

#print(model.predict(12))

MSE=np.mean((15-model.predict(12)[0])**2)
print('Mean Squared Error %r' %(MSE))


import pandas as pd

df = pd.read_csv("Salary_Data.csv")

print (df)

x1 = df['Salary']
y1 = df['YearsExperience']

#print (x1)
#print(y1)

plt.figure()
plt.title('Salary vs Experience')
plt.ylabel('Salary')
plt.xlabel('Years of experience')
plt.plot(x1,y1,'m.')
#plt.axis([0,25,0,25])
plt.grid(True)
plt.show()


from sklearn.cross_validation import train_test_split


#Y = df['Salary']
#X = df['YearsExperience']
X = df.iloc[:,:-1].values
Y = df.iloc[:,1].values


X_train, X_test , y_train , y_test = train_test_split(X,Y,test_size=1/6,random_state =0)
print('y_test')
print(y_test)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)

MSE = np.mean((y_test-y_pred)**2)
print("Mean Squared Error %r" %(MSE))

plt.scatter(X_train,y_train, color ='red')
plt.plot(X_train,regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_test,y_test, color ='red')
plt.plot(X_test,regressor.predict(X_test), color = 'blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
