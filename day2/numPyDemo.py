# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 10:41:52 2018

@author: Administrator
"""

import numpy as np

m = np.array([np.arange(3), np.arange(3)])
print(m)

print(m.shape)


#single precision floats
print(np.arange(7,dtype='f'))

print(np.arange(7,dtype='D'))

a=np.arange(9)

print(a[3:])

print(a[:7:2])

print(a[::-1])


b= np.arange(24).reshape(2,3,4)
print("b")
print(b)
print(b.ravel())#view of original array
print(b.flatten())#flatten return a copy

print("b transpose")

b.shape=(6,4)
print(b)

print(b.transpose())
b.resize((2,12))
print(b)

a =  np.arange(9).reshape(3,3)
print(a)
b=2*a
print(b)
print("horizontal")

#a.resize((2,2))
#print(a)
print(np.hstack((a,b)))
print("concat")


print(np.concatenate((a,b),axis=1))

print(np.vstack((a,b)))

import statistics
data=[0.75,1.00,3.00,-1.50,0.50,2.00]

A=statistics.stdev(data)

print(A)


data1=[1.50,5.00,12.00,-9.00,-4.00,1.50]

B=statistics.stdev(data1)

print(B)

import numpy as np

a = np.array([[0.10,0.14,0.18],[0.01,0.112,0.018]])


var = np.array([3, 7, 8, 5, 12, 14, 21, 13, 18])

a = np.array([1,2,3,4,5])
p= np.percentile(a,50)

print(p)
print("Quartiles...",'',np.percentile(var, 25, interpolation='midpoint'))

var = np.array([400,500,550,600,625,650,725,750,800,800,850,925])
print("Deciles...",'',np.percentile(var, np.arange(0,100,10), interpolation='midpoint'))



