# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 19:47:42 2021

@author: Hayagreev
"""
from sympy import *
import numpy as np
import time
from quantiphy import Quantity as q




t_o = time.time()

n = int(input("Enter the limit:"))

sum=0

for i in range(2,int(n+1)):
    if isprime(i):
        sum+=i

print('Sum:',sum)

t = time.time()

execution_time = t-t_o

print("Execution Time:",q(execution_time,'s'))