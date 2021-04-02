# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 14:09:53 2021

@author: Hayagreev
"""
import time
import math
from quantiphy import Quantity as q




t_o = time.time()



def longestPrimeQuadratic(alim, blim):

    def isPrime(k): # checks if a number is prime
        if k < 2: return False
        elif k == 2: return True
        elif k % 2 == 0: return False
        else: 
            for x in range(3, int(math.sqrt(k)+1), 2):
                if k % x == 0: return False

        return True 

    longest = [0, 0, 0] # length, a, b
    for a in range((alim * -1) + 1, alim):
        for b in range(2, blim):
            if isPrime(b):
                count = 0
                n = 0
                while isPrime((n**2) + (a*n) + b):
                    count += 1
                    n += 1

                if count > longest[0]:
                    longest = [count, a, b]
   
    print(a*b)
    return longest

ans = longestPrimeQuadratic(1000, 1000)




t = time.time()

execution_time = t-t_o

print("Execution Time:",q(execution_time,'s'))