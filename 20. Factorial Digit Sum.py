# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:33:34 2021

@author: Hayagreev
"""

import time
from quantiphy import Quantity as q
import math



t_o = time.time()

n=int(input("Enter a number: "))

sum = 0

N =  list(map(int,str(math.factorial(n))))

for i in range(len(N)):
    sum+= N[i]
    
print("Sum of ",n,"!:",sum)
t = time.time()

execution_time = t-t_o

print("Execution Time:",q(execution_time,'s'))