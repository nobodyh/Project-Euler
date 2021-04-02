# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:14:26 2021

@author: Hayagreev
"""
import numpy as np

n=int(input("Enter the limit:"))

result = np.subtract(np.power(np.divide(np.multiply(n,n+1),2),2),np.divide(np.multiply(n,np.multiply(n+1,2*n+1)),6))

print("Result: ",result)



