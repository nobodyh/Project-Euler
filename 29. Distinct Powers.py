# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 20:15:02 2021

@author: Hayagreev
"""

import time
from quantiphy import Quantity as q



t_o = time.time()

a = int(input("Enter lower limit: "))
b = int(input("Enter upper limit: "))

l=[]

for x in range(a,b+1):
    for y in range(a,b+1):
        l.append(x**y)

result=[]

[result.append(i) for i in l if i not in result]

result.sort()

print("Result:",result)


t = time.time()

execution_time = t-t_o

print("Execution Time:",q(execution_time,'s'))