# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:27:05 2018

@author: Administrator
"""
import datetime


customerList =[[23747,"Anoop",datetime.date(1987,1,1)],
                [23747,"Sunil",datetime.date(1988,4,6)],
                [23747,"Sudeep",datetime.date(2001,5,6)],
                [23747,"Rahul",datetime.date(2005,6,11)]]
                 
for cust in customerList[0:]:
    dob = cust[2].strftime("%d,%m,%Y")
    print ("Customer Name %s DOB %s" %(cust[0], dob))
    
    
    
#zip
projects = ["banking", "insurance", "CreditCard"]
locations = ["Chennai", "Pune", "Bangalore"]
clients = ["HSBC","Royal Sundaram", "VISA"]


for(p,l,c) in zip(projects,locations,clients):
    print(p,"----->", l , "----->", c)
    
print(projects[:-1])
print(locations)
#tuple
gender=("MALE","FEMALE","TRANSGENDER")

#configuration values
configData=(["192.67.89.90","sa","admin@123"],
            ["192.67.91.90","root","admin@123"],
            ["216.67.89.90","sa","admin@123"])

configData[0].append("test")
print(configData[0])



