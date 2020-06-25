#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code may be used freely for any purpose,
as long as this comment is included

Created on Thu Jun 25 16:55:19 2020

@author: Emil Jonathan Eriksson
@author_email: eje1999@gmail.com
"""
from numpy import *
from matplotlib.pyplot import *
import sys

"""
Task 1

"""
def f(fi, r=1):
    return r * exp(1j * fi)

fi_list = linspace(0, 2*pi, num=150)
r_list = linspace(0.1, 1, num=10)
z_real_list = []
z_imag_list = []

for r in r_list:
    for fi in fi_list:
        z = f(fi, r)
        z_real_list.append(z.real)
        z_imag_list.append(z.imag)

plot(z_real_list, z_imag_list)

"""
Task 2

"""    

def newton(f, fp, x0, tol, max_iterations=400):
    x = x0
    for i in range(0, max_iterations):
        x_next = x - f(x)/fp(x)
        if abs(x_next - x) < tol:
            return x_next, True
        else:
            x = x_next
    else:
        return x_next, False  
    
def myfunc(x):
    return x**3 + 4*x**2 + 5*x + 13

def myfuncp(x):
    return 3*x**2 + 8*x + 5

print(newton(myfunc, myfuncp, 1, 1.e-9))




    