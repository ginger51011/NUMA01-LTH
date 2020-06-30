#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code may be used freely for any purpose,
as long as this comment is included

Created on Mon Jun 29 16:53:31 2020

@author: Emil Jonathan Eriksson & Peter Handrup
"""
from numpy import *
from matplotlib.pyplot import *
import sys

"""
Task 1

"""

def approx_ln(x, n=400):
    """A function that approxes ln(x),
    using B.C. Carlssons algorithm
    

    Parameters
    ----------
    x : float
    n : int, optional
        Number of iterations for the 
        approximatio. The default is 400.

    Returns
    -------
    y : float
        An approximation of ln(x)

    """
    
    # The algorithm are defined with these requirements
    if x < 0 or n < 1:
        raise ValueError("x must be larger than 0, n larger or equal to 1")
    
    # Initiating a0 and g0
    a = (1 + x) / 2
    g = sqrt(x)
    
    for i in range(0, n):
        a = (a + g) / 2
        g = sqrt(a * g)
    
    return (x - 1) / a

print(f"{log(8)}, {approx_ln(8, n=1000)}")

"""
Task 2

"""

x_arr = linspace(1, 10, num=200)
x_ln = [log(x) for x in x_arr]
figure(0)
plot(x_arr, x_ln, label=f"ln(x)")

# We want to plot the approximation and difference for 
# different values of n
for n in [1, 2, 3, 5]:
    x_approx_ln = []
    x_diff = []
    
    # The two different values to be added
    # are calculated for the same n
    for x in x_arr:
        x_approx_ln.append(approx_ln(x, n))
    for i in range(0, len(x_arr)):  # We want to calculate for every index of x_arr
        x_diff.append(abs(x_ln[i] - x_approx_ln[i]))
        
    figure(0)
    plot(x_arr, x_approx_ln, label=f"n={n}")
    legend()
    figure(1)
    plot(x_arr, x_diff, label=r"$n=$" + str(n))
    legend()

figure(0)
xlabel(r"$x$")
ylabel(r"$y$")
title(r"Approximations of $\ln{(x)}$")

figure(1)
semilogy()  # We want y axis to be logarithmic
xlabel(r"$x$")
ylabel(r"$|ln(x) - approx\_ln(x)|$")
title("Difference between approximated ln(x) and ln(x) \nfor some number of iterations n")


"""
Task 3

"""

x = 1.41
n_arr = range(1, 7)
x_diff = []

for n in n_arr:
    x_diff.append(abs(log(x) - approx_ln(x, n)))
    
figure(2)
plot(n_arr, x_diff, '*r')
semilogy()  # We want y axis to be logarithmic
xlabel(r"$n$")
ylabel(r"$|ln(x) - approx\_ln(x)|$")
title("Difference between approximation and ln(x) \nfor some number of iterations n")


"""
Task 4

"""

def fast_approx_ln(x, n=5):
    """A fast approximation of ln(x), using
    B.C. Carlssons algorithm

    Parameters
    ----------
    x : float
    n : int, optional
        Number of iterations for the 
        approximatio. The default is 400.

    Returns
    -------
    y : float
        An approximation of ln(x)

    """
    
    if x < 0 or n < 1:
        raise ValueError("x must be larger than 0, n larger or equal to 1")
    
    return (x - 1) / __d(x, n, n)
 
# "__" before function name indicates that this
# should NOT be called outside this module
def __d(x, k, i):
    """Recursive method to find ln(x)
    
        Parameters
    ----------
    x : float
    k : int
    i : int
    
    Returns
    -------
    a : float
        An approximation of ln(x)
    """
    
    if k < 1:   # Basfall, vi når d_0,i
        a = (1 + x) / 2
        g = sqrt(x)
        for n in range(0, i):
            a = (a + g) / 2
            g = sqrt(a * g)
        return a
    else:
        return (__d(x, k - 1, i) - 4**(-k) * __d(x, k - 1, i - 1)) / (1 - 4**(-k))
    

print(f"{log(1.41)}, {fast_approx_ln(x=1.41, n=5)}")


"""
Task 5

"""

for n in [1, 2, 3, 5]:
    x_fast_approx_ln = []
    x_diff = []
    
    for x in x_arr:
        x_diff.append(abs(log(x) - fast_approx_ln(x, n)))
        
    figure(3)
    plot(x_arr, x_diff, label=r"$n=$" + str(n))

figure(3)
semilogy()  # We want y axis to be logarithmic
legend()
xlabel(r"$x$")
ylabel(r"$|ln(x) - approx\_ln(x)|$")
title("Difference between fast_approximated _n(x) and ln(x) \nfor some number of iterations n")