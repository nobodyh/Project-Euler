# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 20:01:26 2021

@author: Hayagreev
"""

import time
from quantiphy import Quantity as q




t_o = time.time()

n = int(input("Enter the Digit Power: "))
sum = 0
i=1
while (i<(10**n)):
    
    digit_sum = 0
    
    j = list(str(i))
    
    for k in j:
        digit = int(k)**n
        digit_sum+= digit
    
    if digit_sum == i:
        sum+=i
        print(i)
    i+= 1

sum-= 1
    
print(sum)

t = time.time()

execution_time = t-t_o

print("Execution Time:",q(execution_time,'s'))