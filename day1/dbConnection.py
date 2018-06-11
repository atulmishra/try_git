# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 16:15:37 2018

@author: Administrator
"""

import pymysql
def createConnection():
    conn = pymysql.connect(host="localhost",user="root",passwd = "root" 
                           , db = "citidb_2018")
                           
    return conn;



def addCustomer(data):
    connObj=createConnection()
    #connObj = connObj.cursor();
    cursor = connObj.cursor();
    print("Cursor ready...");
    try:
             cursor.execute("""insert into Customer values ('%d', '%s', '%s')""" %(data[0],data[1],data[2]));
             connObj.commit()
    except pymysql.Error as e:
              print("Exception Occurred", e)
              connObj.rollback()
            

def selectCustomer(custId):
    connObj=createConnection()
    cursor = connObj.cursor();
    print("Cursor ready...");
    try:
             cursor.execute("""select * from Customer where  Customer_Id = '%d'""" %(custId));
             connObj.commit()
    except pymysql.Error as e:
              print("Exception Occurred", e)
              connObj.rollback()
    return cursor.fetchall()

#import datetime
#customer=[43723,"Sanjay",datetime.date(1987,1,1)]

for row in selectCustomer(43723):
    print(row)

#addCustomer(customer)