#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code may be used freely for any purpose,
as long as this comment is included

Created on Mon Jul  6 09:32:40 2020

@author: Emil Jonathan Eriksson
@author_email: eje1999@gmail.com
"""
from numpy import *
from matplotlib.pyplot import *
import sys
from scipy.optimize import fsolve

"""
Task 1

"""

f = lambda x: 3*x**3 - x**2 - 23*x + 3
fp = lambda x: 9*x**2 - 2*x - 23 # Could be replaced by numerical calculation

ax = subplot()

x_arr = linspace(-5, 5)
f_arr = []
fp_arr = []

for x in x_arr:
    f_arr.append(f(x))
    fp_arr.append(fp(x))

poly_line, = ax.plot(x_arr, f_arr, label="polynomial")
deriv_line, = ax.plot(x_arr, fp_arr, label="derivative")
ax.legend()


"""
Task 2

"""

# Might be a bad way of solving this,
# did not find fitting built-in Python functions
def get_tangent(f, x0, h=1.e-7):
    """
    Returns a function that is the approximation of a tangent
    at the point x0 for the function f

    Parameters
    ----------
    f : function
        Function to be evaluated.
    x0 : float
        Point of sdasdldsaj engelska dåligt.
    h : float, optional
        Step size. The default is 1.e-7.

    Returns
    -------
    tangent : function
        tangent(x) = k*x+m.

    """
    
    return lambda x: ( (f(x0 + h) - f(x0)) / h) * x + f(x0)

fpp = lambda x: 18*x -2 # Don't do this, it feels really weird

# These two are used in Task 7
x_ticks = []
y_ticks = []

# This is a really sketchy solution to this problem
for x0 in fsolve(fpp, 0):
    print(f"Inflection point at {x0}...")
    x_tangent = []
    tangent = get_tangent(f, x0)
    interval = linspace(x0 - 2, x0 + 2)
    x_ticks.append(x0)
    y_ticks.append(f(x0))
    for x in interval:
        x_tangent.append(tangent(x))
    plot(interval, x_tangent, label="tangent")
    

"""
Task 3

"""

# This is also a really sketchy solution to this problem
for x0 in fsolve(fp, [-100, 100]):
    print(f"Extremal value at {x0}...")
    x_tangent = []
    tangent = get_tangent(f, x0)
    interval = linspace(x0 - 2, x0 + 2)
    x_ticks.append(x0)
    y_ticks.append(f(x0))
    for x in interval:
        x_tangent.append(tangent(x))
    plot(interval, x_tangent, label="tangent")
    

"""
Task 4

"""

# This is why we gave them all the "tangent" label
# earlier
for line in ax.lines:
    if line.get_label() == "tangent":
        line.set_color("black")
        line.set_linestyle(":")
  
      
"""
Task 5

"""

poly_line.set_linewidth(3.3)


"""
Task 6

"""

ax.annotate("A random point on the polynomial", xy=(4, f(4)),
            xytext = (0, f(0) - 200),
            arrowprops = {"facecolor": "black", "shrink": 0.006})

x_ticks.append(4)
y_ticks.append(f(4))

"""
Task 7

"""

# This was added in the foor-loops in Tasks 3 and 4
ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)


"""
Task 8

"""

ax.set_title(r"Plot of $3x^3-x^2-23x+3$")


"""
Task 9

"""

# savefig("spam.png")