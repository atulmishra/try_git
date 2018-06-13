# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 15:14:32 2018

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig = plt.figure()
fig.add_axes([0,0,1,1])

plt.show()

plt.plot([1,2,3],[4,5,1])


plt.show()

x=[5,8,10]
y=[12,16,6]

plt.plot(x,y)

plt.title("Epic info")
plt.ylabel('Y axis')
plt.xlabel('X Axis')
plt.legend()

plt.grid(True,color='k')
from matplotlib import style

style.use('ggplot')

x =[5,8,10]
y = [12,16,6]

x2=[6,9,11]
y2 = [6,15,7]

plt.plot(x,y,'g',label='line one', linewidth=5)
plt.plot(x2,y2,'c',label='line two', linewidth=5)

plt.title("Epic info")
plt.ylabel('Y axis')
plt.xlabel('X Axis')
plt.legend()

plt.grid(True,color='k')
plt.show()

plt.bar(x, y, align='center')

plt.bar(x2, y2, color='g', align='center')


plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()


df = pd.read_csv("diabetes.csv")

x = df["BMI"]
y=df["Glucose"]
y1=df["BloodPressure"]
plt.scatter(x , y , color='g')

plt.scatter(x , y1 , color='m')
plt.show()



#df = pd.read_csv("Data.csv")

x2= ['India','Sri Lanka', 'USA', 'UK']
x1= [10,20,30,40]
y = [1,5,3,4]
plt.plot(x1,y)
plt.xticks(x1,x2)
plt.show()
