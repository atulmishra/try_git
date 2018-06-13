# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 16:51:21 2018

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np


plt.hist([1,11,12,14,21,31,41], bins=[0,10,20,30,40,50], weights=[10,10,7,5,40,33,6])
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")