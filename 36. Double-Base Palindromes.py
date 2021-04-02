# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 11:19:07 2021

@author: Hayagreev
"""
import time
from quantiphy import Quantity as q

def isPalindrome(s):

    # Using predefined function to
    # reverse to string print(s)
    rev_decimal = ''.join(reversed(str(s)))
    rev_binary = ''.join(reversed(bin(int(s)).replace("0b", "")))
    
    #print("s:",s,"   r_s:",rev_decimal)
    #print("Binary: ",bin(int(s)).replace("0b", ""),"  R_B: ",rev_binary)
    # Checking if both string are
    # equal or not
    if (str(s) == rev_decimal and str(bin(s).replace("0b", "")) == str(rev_binary)):
        #print("Yes")
        return 1
    else:
        #print("No")
        return 0


t_o = time.time()

n = int(input("Enter the limit: "))

sum = 0

for i in range(1,n):
    
    flag = isPalindrome(i)
    
    if (flag == 1):
        sum+= i

print("Sum: ",sum)

t = time.time()

execution_time = t-t_o

print("Execution Time:",q(execution_time,'s'))
