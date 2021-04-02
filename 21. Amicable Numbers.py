# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 20:50:03 2021

@author: Hayagreev
"""

import time
from quantiphy import Quantity as q


def SD(x):
    
    sum = 0
    
    for i in range(1,x):
        if(x%i)==0:
            sum+= i
    
    return sum

t_o = time.time()


result = []

n = int(input("Enter the limit:"))

for i in range(1,n):
    a=i
    da=SD(i)
    b=da
    db=SD(b)
    
    if (da==b and db==a and a!=b):
        if([a,b] not in result and [b,a] not in result):
            print("a:",a," and b:",b)
            result.append([a,b])
    
print(result)

t = time.time()

execution_time = t-t_o

print("Execution Time:",q(execution_time,'s'))