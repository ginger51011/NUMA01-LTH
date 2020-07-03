#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code may be used freely for any purpose,
as long as this comment is included

Created on Fri Jul  3 14:57:37 2020

@author: Emil Jonathan Eriksson
@author_email: eje1999@gmail.com
"""
from numpy import *
from matplotlib.pyplot import *
import sys

"""
Task 1

"""

yearmonthday = []
kwh = []

with open("../data/kwh.dat") as f:
    for line in f.readlines():
        split_line = line.split()
        yearmonthday.append(split_line[0])
        kwh.append(int(split_line[1]))


"""
Task 2

"""

yearmonthday.reverse()
kwh.reverse()


"""
Task 3

"""

monthly_usage = diff(array(kwh))

"""
Task 5

"""

# I think the first value of yearmonthday should be removed,
# monthly_usage has one element less
plot(yearmonthday[1:], monthly_usage, 'r-')
title("Monthly energy consumtion for Claus")
xticks(arange(0, 150, step=9), rotation=60)

max_power_usage = max(monthly_usage)
max_power_usage_index = where(monthly_usage == max_power_usage)[0][0]
max_power_date = yearmonthday[max_power_usage_index]

print(f"Max power usage was at {max_power_date} with a usage of {max_power_usage} kWh")


min_power_usage = min(monthly_usage)
min_power_usage_index = where(monthly_usage == min_power_usage)[0][0]
min_power_date = yearmonthday[min_power_usage_index]

print(f"Min power usage was at {min_power_date} with a usage of {min_power_usage} kWh")

"""
Task 6

"""

max_increase_indexes = []
max_decrease_indexes = []
max_increase = 0
max_decrease = 0

for i in range(1, len(monthly_usage)):
    diff = monthly_usage[i] - monthly_usage[i - 1]
    if diff > max_increase:
        max_increase = diff
        max_increase_indexes = [i - 1, i]
    if diff < max_decrease:
        max_decrease = diff
        max_decrease_indexes = [i - 1, i]
        
print(f"The largest increase in power consumtion was between {yearmonthday[max_increase_indexes[0]]}\n\
      and {yearmonthday[max_increase_indexes[1]]} with an increase of {max_increase} kWh")
print(f"The largest decrease in power consumtion was between {yearmonthday[max_decrease_indexes[0]]}\n\
      and {yearmonthday[max_decrease_indexes[1]]} with an decrease of {max_decrease} kWh")
     

"""
Task 7

"""

print(f"Mean power consumtion per month was about {round(mean(monthly_usage))} kWh")






