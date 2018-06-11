# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 17:11:37 2018

@author: Administrator
"""
from oopsDemo import Product

class SeasonalProduct(Product):
    
    def __init__(self, id, name , dop ,period):
        Product.__init__(self, id , name, dop)
        self.__period = period

import datetime

obj = SeasonalProduct(31254,"Coke",datetime.date(2018,6,8),"Summer")     
print(obj.getProductId())