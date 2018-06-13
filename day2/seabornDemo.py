# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 16:25:29 2018

@author: Administrator
"""

import seaborn as sb
import numpy as np
import pandas as pd
from  matplotlib import pyplot as plt

df = sb.load_dataset('iris')
sb.stripplot(x ="species" ,y = "petal_length", data = df)
plt.show()



