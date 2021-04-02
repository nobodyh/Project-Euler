# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:43:26 2021

@author: Hayagreev
"""

import time
from quantiphy import Quantity as q
from datetime import date



t_o = time.time()

count = 0
year = 1901
month = 1

curr_day = date(year,month,1)

while(curr_day.year < 2001):
	if(curr_day.weekday() == 6):
		count += 1
	if(month+1 == 13):
		month = 1
		year += 1
	else:
		month += 1
	curr_day = date(year,month,1)

print("count: " + str(count))



t = time.time()

execution_time = t-t_o

print("Execution Time:",q(execution_time,'s'))