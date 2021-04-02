# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 19:38:45 2021

@author: Hayagreev
"""

import numpy as np
import time
from quantiphy import Quantity as q

t_o = time.time()

sum = int(input("Enter the sum limit:"))
result = int(0)
for a in range(3,sum):
    for b in range(a+1,sum-1):
        c = np.sqrt(np.add(np.power(a,2),np.power(b,2)))
        
        if (a+b+c == sum):
            result = a*b*c
            break
            
print('a: ',a,'   b: ',b,'   c: ',c)
print('Result:',result)    

t = time.time()

execution_time = t-t_o

print("Execution Time:",q(execution_time,'s'))