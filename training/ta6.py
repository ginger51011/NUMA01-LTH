#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code may be used freely for any purpose,
as long as this comment is included

Created on Tue Jun 30 16:44:15 2020

@author: Emil Jonathan Eriksson
@author_email: eje1999@gmail.com
"""
from numpy import *
from matplotlib.pyplot import *
import sys

"""
Task 1

"""

def is_symmetric(A):
    At = A.T
    
    if A.all() == At.all():
        return 1
    elif A.all() == -At.all():
        return -1
    else:
        return 0

A = array([[1, 7, 3],
          [7, 4, -5],
          [3, -5, 6]])

print(f"{str(A)} is symmetric, does the function work: {is_symmetric(A) == 1}")


"""
Task 2

"""

