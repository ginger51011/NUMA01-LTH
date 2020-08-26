#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code may be used freely for any purpose,
as long as this comment is included

Created on Thu Jul  9 09:49:57 2020

@author: Emil Jonathan Eriksson
@author_email: eje1999@gmail.com
"""
from numpy import *
from matplotlib.pyplot import *
import sys

from scipy.misc import derivative as derive

"""
CODE COPIED FROM TA11,
MODIFICATIONS MADE IN OLD CODE

"""

"""
Task 1 & 2

"""

# One could just write it out, but that's
# just boring
def taylor_poly(f, x, w, order, a): # w added
    """
    Creates a Taylor polynomial of order order
    for sin(x) around point
    
    """
    if order < 1:
        raise ValueError("Order must be larger than 1")
    
    Tp = f(w*a)
    fact = 1
    
    for i in range(1, order + 1):
        Tp = Tp + ((w*x - a)**i / (fact * i)) * derive(f, x0=w*a, n=i)
    
    return Tp

"""
Most ta12 changes below

"""

ax = subplot()

# Defining our slides
sld_w_ax = axes([-0.5 , 0.3, 0.3, 0.03])
sld_x_ax = axes([-0.5 , 0.2, 0.3, 0.03])

# Create x-values
x_arr = linspace(0, 2 * pi, 600)

# Initial values for sliders
w0, x0 = 1., pi / 2

# Creating sliders
sld_w = Slider(sld_w_ax, r"$\omega$", 0, 2 * pi, valinit=w0, valfmt="%1.3f")
sld_x = Slider(sld_x_ax, r"$x_0$", 0, 2 * pi, valinit=x0, valfmt="%1.3f")

# Settings for plot
ax.set_xlim([0, 2 * pi])
ax.set_ylim([-1.2, 1.2])
ax.set_aspect(1.0)


# Plot our lines, using initial values
sin_line = ax.plot(x_arr, sin(w0 * x_arr), label=r"$sin(\omega x)$")
T_line = ax.plot(x_arr, taylor_poly(sin, x_arr, w0, 2, x0), label=r"$T_2(\omega x)$ around $x_0$")

# Callback functions to handle updated sliders
def update_curve(val):
    new_x = sld_x.val
    new_w = sld_w.val
    
    sin_line.set_ydata(sin(new_w * x_arr))
    T_line.set_ydata(taylor_poly(sin, x_arr, new_w, 2, new_x))

sld_w.on_changed(update_curve)
sld_x.on_changed(update_curve)

"""
Task 3

"""
ax.set_xticks([0, pi/2, pi, 3*pi/2, 2*pi])
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.legend()


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
ax.set_title(r"Curves in $[0, 2\pi]$ for $sin(\omega x)$, with Taylor polynomial $T_n(x)$" + "\n" + r"of second order around $x_0$")



