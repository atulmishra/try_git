# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#identifier declaration


organizationName = "Citi Corp"


firstName="Atul"
print("Organization Name =%s \n First Name= %s"  %(organizationName, firstName))
#type checking
print (type(organizationName))
#age = int(input("Enter Age"))
age=47
print(type(age))
import datetime

dob = datetime.date(2018,11,6)

strdob = dob.strftime("%A,%B,%Y")
print("DOB=%s" %(str(strdob)))
#binary conversion
print(bin(3856))

print(int('111100010000',2))
#complex number
print(complex(45,67))