# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 13:31:01 2021

@author: Hayagreev
"""
import numpy as np
def Prime_Factors(x):
    factors=[]
    
    while x%2==0:
        factors.append(2)
        x/= 2
    
    for i in range(3,int(np.sqrt(x))+1,2):
        
        while x%i==0:
            factors.append(i)
            x/= i
    
    return factors

x = int(input("Enter a number: "))

factors = Prime_Factors(x)

max_factor = max(factors)

print("Maximum Factor: ",max_factor)