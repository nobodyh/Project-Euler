# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:54:21 2021

@author: Hayagreev
"""

import time
from quantiphy import Quantity as q
from num2words import num2words



t_o = time.time()

n = int(input("Enter the limit: "))
result = 0
for i in range(1,n + 1):
   result+=(len(''.join(''.join(num2words(i).split('-')).split(' '))))

print("Result: ",result)

t = time.time()

execution_time = t-t_o

print("Execution Time:",q(execution_time,'s'))