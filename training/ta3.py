#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code may be used freely for any purpose,
as long as this comment is included

Created on %(date)s

@author: Emil Jonathan Eriksson
@author_email: eje1999@gmail.com
"""
from numpy import *
from matplotlib.pyplot import *
import sys


"""
Task 1

"""

# 0
# 0
# [0,1,2,1,0,-1,-2,-1]
# append typ
# Nothing changes
# 3 tas bort ur listan
# element 2, 3 och 4 byts ut mot -5.


"""
Task 2

"""

# print(f()) ger ett error, krävs en parameter
# print(f) blir lite konstig, man skriver 
# ju ut referensvariabeln.

"""
Task 3

"""

def f(m):
    """
    L[0] == -m/2
    L[-1] == (m-1)-m/2
    => 1 + L[0] + L[-1] == 1 - m/2 + m - 1 - m/2 == 0
    
    dvs. skriver ut 0.

    """
    L = [n-m/2 for n in range(m)]
    return 1 + L[0] + L[-1]

print([f(m) for m in range(1, 30)])

def f_fixed(m):
    """
    Skriver ut varannan etta.

    """
    L = [n-m//2 for n in range(m)]
    return 1 + L[0] + L[-1]

print([f_fixed(m) for m in range(1, 30)])


"""
Task 4

"""

distance = [[0, 20, 30, 40],
            [20, 0, 50, 60],
            [30, 50, 0, 70],
            [40, 60, 70, 0]]

reddistance_loop = []
for list in distance:
    newlist = []
    for i in list:
        if i == 0:
            break
        else:
            newlist.append(i)
    reddistance_loop.append(newlist)

print(f"Looped list is {reddistance_loop}")

# Osexigaste lösningen någonsin
reddistance_slice = [distance[1][0:1], distance[2][0:2], 
                     distance[3][0:3]]
print(f"Sliced list is {reddistance_slice}")

def sydiff(a, b):
    if not isinstance(a, set) or not isinstance(b, set):
        raise TypeError("sydiff must be called on two sets")
        
    return sorted(a.difference(b).union(b.difference(a)))

a = {1, 16, 2, 3, 5, 8, 13}
b = {2, 5, 6, 13, 17}

print(f"sydiff returns {sydiff(a, b)}")
print(f"Built in method returns {a.symmetric_difference(b)}")

"""
Task 6

"""

# intersection returns a new set,
# intersection_update edits the current set

"""
Task 7

"""

empty_set = set([])
print(f"Is the empty set a subset of {a}: {empty_set.issubset(a)}")
print(f"Is the empty set a subset of {b}: {empty_set.issubset(b)}")


"""
Task 8

"""

def bisec(i, tol):
    """
    

    Parameters
    ----------
    i : list
        The interval between which the operation is made.
    tol : float
        Tolerance.

    Returns
    -------
    Final interval, midpoint.

    """
    i = sort(i)
    a, b = i[0], i[-1]
    
    if a * b > 0:
        ValueError("Does not change sign")
        
    while (b - a) > tol:
        i_low = [a, (a + b) / 2]
        i_high = [(a + b) / 2, b]
        
        if i_low[0] * i_low[-1] < 0:
            b = (a + b) / 2
        else:
            a = (a + b) / 2
            
    return [a, b], (a + b) / 2

i1 = [-0.5, 0.6]
i2 = [-1.5, -0.4]

def poly(x):
    return 3 * x**2 - 5

p_i1_bisec = bisec([poly(i1[0]), poly(i1[-1])], 1.e-5)
p_i2_bisec = bisec([poly(i2[0]), poly(i2[-1])], 1.e-5)

print(f"Polynomial in interval {i1} gives bisec result as {p_i1_bisec}")
print(f"Polynomial in interval {i2} gives bisec result as {p_i2_bisec}")

a_i1_bisec = bisec([arctan(i1[0]), arctan(i1[-1])], 1.e-5)
a_i2_bisec = bisec([arctan(i2[0]), arctan(i2[-1])], 1.e-5)

print(f"Arctan in interval {i1} gives bisec result as {a_i1_bisec}")
print(f"Arctan in interval {i2} gives bisec result as {a_i2_bisec}")


"""
Task 9

"""

def bisec(function, i, tol):
    i = sort(i)
    a, b = function(i[0]), function(i[-1])
    
    if a * b > 0:
        ValueError("Does not change sign")
        
    while (b - a) > tol:
        i_low = [a, (a + b) / 2]
        i_high = [(a + b) / 2, b]
        
        if i_low[0] * i_low[-1] < 0:
            b = (a + b) / 2
        else:
            a = (a + b) / 2
            
    return [a, b], (a + b) / 2


