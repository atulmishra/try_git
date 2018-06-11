# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:00:28 2018

@author: Administrator
"""

firstName="atulMIshra"
print(firstName.capitalize())


for _ in firstName[4:2]:
    print(_)
    
    
import random

randomList = []; #List

for _ in range(1,100):
    temp = random.randint(10,10000)
    if(temp > 5000):
        randomList.append(temp)
        
randomList.sort()

import base64

seqNo = 567

pnrNo = base64.b64encode(str(seqNo).encode(encoding= 'utf-8', errors='strict'))

print(pnrNo)
#decoded = base64.b64decode(int(pnrNo).decode(encoding= 'utf-8', errors='strict'))
#print(decoded)

print(firstName.center(len(firstName)+25,"*"))

print(firstName.ljust(len(firstName)+25,"*"))

print(firstName.rjust(len(firstName)+25,"*"))