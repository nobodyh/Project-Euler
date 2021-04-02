# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 13:48:24 2021

@author: Hayagreev
"""

def LP(n):
    UL = (10**n)-1
    
    LL = 1+UL//10
    
    max_product=0
    
    for i in range(UL,LL-1,-1):
        
        for j in range(i,LL-1,-1):
            
            product = i*j
            
            if product<max_product:
                break
            
            number = product
            
            reverse=0
            
            while(number!=0):
                
                reverse = reverse*10 + number%10
                
                number = number//10
                
                if (product == reverse and product>max_product):
                    
                    max_product = product

    return i,j,max_product

n=int(input("Enter the n-digit value to determine Largest Palindrome:"))

a,b,Result=LP(n)

print("a:",a,"\nb:",b,"\nProduct:",Result)       