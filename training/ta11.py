#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code may be used freely for any purpose,
as long as this comment is included

Created on Wed Jul  8 14:20:22 2020

@author: Emil Jonathan Eriksson
@author_email: eje1999@gmail.com
"""
from numpy import *
from matplotlib.pyplot import *
import sys
from scipy.misc import derivative as derive

"""
Task 1 & 2

"""

# One could just write it out, but that's
# just boring
def taylor_poly(f, x, order, a):
    """
    Creates a Taylor polynomial of order order
    for sin(x) around point
    
    """
    if order < 1:
        raise ValueError("Order must be larger than 1")
    
    Tp = f(a)
    fact = 1
    
    for i in range(1, order + 1):
        Tp = Tp + ((x - a)**i / (fact * i)) * derive(f, x0=a, n=i)
    
    return Tp

x_arr = linspace(0, 2 * pi)
x_arr1 = []
x_arr2 = []

sin_arr = []
T1_arr = []
T2_arr = []

for x in x_arr:
    sin_arr.append(sin(x))
    if abs(taylor_poly(sin, x, 2, pi / 2) - sin(x)) < 0.2:
        x_arr1.append(x)
        T1_arr.append(taylor_poly(sin, x, 2, pi / 2))
    if abs(taylor_poly(sin, x, 2, 3*pi / 2) - sin(x)) < 0.2:
        x_arr2.append(x)
        T2_arr.append(taylor_poly(sin, x, 2, 3*pi / 2))
    
ax = subplot()

sin_plot = ax.plot(x_arr, sin_arr, 'r-', label=r"$sin(x)$")
T1_plot = ax.plot(x_arr1, T1_arr, 'b-')
T2_plot = ax.plot(x_arr2, T2_arr, 'g-')

# We need to compensate for sin(x) being plotted for more than x_arr1 and x_arr2,
# and also x_arr1 + x_arr2 > x_arr
ax.fill_between(x_arr1, sin_arr[:len(x_arr1)], T1_arr,color = "black", alpha = 0.3)
ax.fill_between(x_arr2, sin_arr[len(x_arr1) - 2:], T2_arr,color = "black", alpha = 0.3) # skeeeetchy


"""
Task 3

"""
ax.set_xticks([0, pi/2, pi, 3*pi/2, 2*pi])
ax.set_yticks([-1, -0.5, 0, 0.5, 1])


"""
Task 4

"""

# I litterally copypasted code from ta10 here...
ax.annotate(r"$\sin(\pi)$", xy=(pi, sin(pi)),
            xytext = (pi / 2, -0.5),
            arrowprops = {"facecolor": "black", "shrink": 0.005,
                          "width": 0.75, "headwidth": 7.5})
ax.annotate(r"$T_2(0)$, around $\frac{\pi}{2}$", xy=(0, taylor_poly(sin, 0, 2, pi / 2)),
            xytext = (pi / 2 -0.5, -0.75),
            arrowprops = {"facecolor": "black", "shrink": 0.005,
                          "width": 0.75, "headwidth": 7.5})
ax.annotate(r"$T_2(pi)$, around $\frac{3\pi}{2}$", xy=(pi, taylor_poly(sin, pi, 2, 3*pi / 2)),
            xytext = (3*pi / 2, 0.5),
            arrowprops = {"facecolor": "black", "shrink": 0.005,
                          "width": 0.75, "headwidth": 7.5})

"""
Extra fluff

"""
ax.set_title(r"Curves in $[0, 2\pi]$ for sin(x), with Taylor polynomials $T_n(x)$" + "\n of second order around two points")






















