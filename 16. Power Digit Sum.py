# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:59:53 2021

@author: Hayagreev
"""

import time
from quantiphy import Quantity as q




t_o = time.time()

a = int(input("Enter a:"))
b = int(input("Enter b:"))

sum = 0
x = list(map(int,str(a**b)))

for i in range(len(x)):
    sum+= x[i]

print("Sum: ",sum)

t = time.time()

execution_time = t-t_o

print("Execution Time:",q(execution_time,'s'))