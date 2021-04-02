# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 20:25:58 2021

@author: Hayagreev
"""

import time
import numpy as np
from quantiphy import Quantity as q


def Fn(x):
    return (int(np.multiply(np.divide(1,np.sqrt(5)),np.subtract(np.power((np.divide(np.add(1,np.sqrt(5)),2)),x),np.power((np.divide(np.subtract(1,np.sqrt(5)),2)),x)))))

t_o = time.time()

flag=0
i=1

digit=int(input("Enter the digit size:"))

while flag!=1:
    if(len(str(Fn(i)))==digit):
        flag = 1
        break
    i+= 1
    
print(i)    

t = time.time()

execution_time = t-t_o

print("Execution Time:",q(execution_time,'s'))