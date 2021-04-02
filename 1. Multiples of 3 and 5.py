# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 11:13:40 2021

@author: Hayagreev
"""

sum=0

for i in range(1,1000,1):
    if (i%3)==0 or (i%5)==0:
        sum+=i

print('Sum:',sum)