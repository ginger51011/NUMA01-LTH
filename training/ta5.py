#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code may be used freely for any purpose,
as long as this comment is included

Created on Fri Jun 26 16:52:30 2020

@author: Emil Jonathan Eriksson
@author_email: eje1999@gmail.com
"""
from numpy import *
from matplotlib.pyplot import *
import sys
from scipy.integrate import quad

"""
Task 1

"""

def get_function(omega):
    # def f(x):
    #   sin(omega * x)
    # är samma sak som
    # lamda x: sin(omega * x)
    return lambda x: sin(omega * x)

f = get_function(2 * pi)

print(quad(f, 0, pi / 2))


