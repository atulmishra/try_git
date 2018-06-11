# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 16:53:45 2018

@author: Administrator
"""

class Product:
    GST = 0.09
    def __init__(self,id,name,dop):
        self.__productId = id
        self.__name = name
        self.__dop = dop
    
    def getProductId(self):
        return self.__productId
    
    def setPrice(self,price):
        self.__price=price
    
    def getPrice(self):
        return self.__price
    @staticmethod
    def computeTotalCost(price):
        return price+price*Product.GST
    
    @staticmethod
    def computeTotalCostWithoutPrice():
        return Product.GST





#import datetime
#obj= Product(42656,"CreditCard",datetime.date(2017,12,12))
#print(obj.getProductId())
##print(obj.__productId)
#
#obj.setPrice(123)
#
#print(obj.getPrice())
#print(Product.GST)
#print(Product.computeTotalCost(obj.getPrice()))
