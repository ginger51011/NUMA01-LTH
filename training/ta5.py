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
from scipy.optimize import fsolve

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


"""
Task 2

"""

omega_arr = linspace(0, 2 *pi, num=1000)
integral_list = []

for omega in omega_arr:
    f = get_function(omega)
    integral_list.append(quad(f, 0, pi / 2))

figure(0)
plot(omega_arr, integral_list)

# LaTeX <3
xlabel(r"$\omega$")
ylabel(r"$\int_0^{\frac{\pi}{2}} \sin{(\omega x)}dx$")
title(r"Value of integral in interval [0, $\frac{\pi}{2}$]")


"""
Task 3

"""

p = lambda x: x**2 + x - 3
print(f"A positive zero of x**2 + x - 3 * pi is {fsolve(p, 1.e23)}")



# More fun
f = lambda x: (x**3) * exp(3*x**2) + 13 * pi
print(f"A zero of (x**3) * exp(3*x**2) + 13 * pi is {fsolve(f, 1)}")


"""
Task 4

"""

# This should be illegal
def get_poly(a):
    return lambda x: a*x**2 + x - 3
    
a_arr = linspace(1, 5, num=150)
root_arr = []

for a in a_arr:
    p = get_poly(a)
    root_arr.append(fsolve(p, 1.e23))

figure(1)
plot(a_arr, root_arr)
xlabel(r"$a$")
ylabel(r"$Positive root$")
title(r"Positive roots for $ax^2+x-3$ for $a\in [1, 5]$")
    
# Knappast linjärt


