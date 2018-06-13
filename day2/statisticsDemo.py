# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 09:59:59 2018

@author: Administrator
"""

import statistics

print (statistics.mean([1,2,3,4,4]))
print (statistics.mean([-1.0,2.5,3.25,5.75]))


from fractions import Fraction as F 
print(statistics.mean([F(3,7),F(1,21),F(5,3),F(1,3)]))
print (F(3,67))

from decimal import Decimal as D

print(statistics.mean([D("0.5"), D("0.75"), D("0.58")]))



print(statistics.harmonic_mean([2.5,3,10]))

print(statistics.median([1,3,4,5]))

print(statistics.median_high([1,3,5,7]))

print(statistics.median_low([1,3,5,7]))

#used in frequency table
print(statistics.median_grouped([52,52,53,54]))

#mode
print(statistics.mode(["red","blue","blue","red","green","red","red"]))
print(statistics.mode([1,1,2,2,2]))



