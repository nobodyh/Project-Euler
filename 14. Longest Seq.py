# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 09:35:11 2021

@author: Hayagreev
"""

import time
from quantiphy import Quantity as q




t_o = time.time()

maximum = 0
seq = []
l=[]

n=int(input("Enter the limit: "))

for i in range(n,n+1):
    x = i
    flag = 0
    
    in_seq = []
    
    while (flag == 0):
        
        if x!=1:
            if (x%2!=0):
                x = 3*x+1
                in_seq.append(x)
            
            elif (x%2==0):
                x = x/2
                in_seq.append(x)
                
        if (x==1):
            flag = 1

    seq=[i,len(in_seq)]
    l.append(seq)

for i in range(len(l)):
    if l[i]>maximum:
        maximum = i

print("The Largest Collatz Sequence: ",maximum+1)



t = time.time()

execution_time = t-t_o

print("Execution Time:",q(execution_time,'s'))