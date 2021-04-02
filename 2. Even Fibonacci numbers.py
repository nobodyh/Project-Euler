# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 11:15:44 2021

@author: Hayagreev
"""
import numpy as np

def Fn(n):
    return int(np.multiply(np.divide(1,np.sqrt(5)),np.subtract(np.power((np.divide(np.add(1,np.sqrt(5)),2)),n),np.power((np.divide(np.subtract(1,np.sqrt(5)),2)),n))))

sum=0
a,b,c,d=1,1,1,0

F=[[a,b],[c,d]]

#a: F_(n+1)
#b: F_n
#c: F_n
#d: F_(n-1)

n=int(input("Enter the nth value:"))

for i in range(n-1):
    F=np.matmul(F,F)
    F_n=Fn(i)
    
    if F_n%2==0:
        sum+=F_n

#print("F_(n):",F[1,0],"F_(n-1):",F[1,1],"F_(n+1):",F[0,0])





print(sum)