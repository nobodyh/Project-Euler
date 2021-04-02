2# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:03:24 2021

@author: Hayagreev
"""
import math

def LCM(n):
    
    ans = 1
    
    for i in range(1,n+1):
        
        ans = int((ans * i)/math.gcd(ans, i))        
    
    return ans


n=int(input("Enter n:"))

result=LCM(n)

    

print(result)