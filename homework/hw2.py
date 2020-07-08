#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code may be used freely for any purpose,
as long as this comment is included

Created on Tue Jul  7 11:19:34 2020,
with a quick break for lunch

@author: Emil Jonathan Eriksson
@author_email: eje1999@gmail.com
"""
from numpy import *
from matplotlib.pyplot import *
import sys

class Interval():
    """
    Represent an interval of two real numbers,
    left and right endpoints. Right is optional.
    
    """
    
    def __init__(self, left, *right):
        """
        

        Parameters
        ----------
        left : int, float
            Leftmost (lower) endpoint for interval.
        *right : int, float, optional
            Rightmost (upper) endpoint for interval.

        Raises
        ------
        ValueError
            If more than one upper endpoint is passed, or if left > right.

        """
        # If right is not passed
        if not right:
            self.left = left
            self.right = left
            return
        # If more than one right is passed
        elif len(right) > 1:
            raise ValueError("Only 1 right argument may be passed")
        # If only one right is passed, we unpack the tuple
        else:
            right, = right
        if left > right:
            raise ValueError("Left bound must be to the left")
        self.left = left
        self.right = right
    
    def __add__(self, other):
        """
        

        Parameters
        ----------
        other : Interval, int or float
            A value to be added to the interval.

        Raises
        ------
        TypeError
            If other is neither Interval, int nor float.

        Returns
        -------
        Interval

        """
        if isinstance(other, Interval):
            return Interval(self.left + other.left, self.right + other.right)
        elif isinstance(other, int) or isinstance(other, float):
            return Interval(self.left + other, self.right + other)
        else:
            raise TypeError(f"Interval may only be added to Interval, float or int; not {type(other)}")
    
    # For example, 1 + Instance(1, 1) will try 1.__add__(Instance(1, 1)) -> TypeError
    # so then Python will try Instance(1, 1).__radd__(1), which should in fact just be
    # just Instance(1, 1).__add__(1)
    def __radd__(self, other):
        return self.__add__(other)
            
    def __sub__(self, other):
        """
        

        Parameters
        ----------
        other : Interval, int or float
            A value to be subtracted with the interval.

        Raises
        ------
        TypeError
            If other is neither Interval, int nor float.

        Returns
        -------
        Interval

        """
        if isinstance(other, Interval):
            return Interval(self.left - other.right, self.right - other.left)
        elif isinstance(other, int) or isinstance(other, float):
            return Interval(self.left - other, self.right - other)
        else:
            raise TypeError(f"Interval may only be subtracted with Interval, float or int; not {type(other)}")
    
    # Compare to __radd__
    # 1.__sub__(2) != 2.__sub__(1), so we must instead
    # make an interval out of other (an int or float)
    # so that other.__sub__(self) becomes possible
    def __rsub__(self, other):
        return Interval(other).__sub__(self)
    
    def __mul__(self, other):
        """
        

        Parameters
        ----------
        other : Interval, int or float
            A value to be multiplied to the interval.

        Raises
        ------
        TypeError
            If other is neither Interval, int nor float.

        Returns
        -------
        Interval

        """
        if isinstance(other, Interval):
            # To make this readable
            a, b, c, d = self.left, self.right, other.left, other.right
            possible_combinations = [a*c, a*d, b*c,b*d]
            new_left = min(possible_combinations)
            new_right = max(possible_combinations)
            return Interval(new_left, new_right)
        elif isinstance(other, int) or isinstance(other, float):
            return Interval(self.left * other, self.right * other)
        else:
            raise TypeError(f"Interval may only be multiplicated with Interval, float or int; not {type(other)}")
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """
        

        Parameters
        ----------
        other : Interval, int or float
            A value to be divided with the interval.

        Raises
        ------
        TypeError
            If other is neither Interval, int nor float.

        Returns
        -------
        Interval

        """
        if isinstance(other, Interval):
            if other.left <= 0 <= other.right:
                raise ValueError("Zero in interval, division by zero extremely illegal")
            a, b, c, d = self.left, self.right, other.left, other.right
            possible_combinations = [a/c, a/d, b/c,b/d]
            new_left = min(possible_combinations)
            new_right = max(possible_combinations)
            return Interval(new_left, new_right)
        elif isinstance(other, int) or isinstance(other, float):
            if other == 0.:
                raise ValueError("Division by zero")
            return Interval(self.left / other, self.right / other)
        else:
            raise TypeError(f"Interval may only be multiplicated with Interval, float or int; not {type(other)}")
    
    def __contains__(self, other):
        """
        

        Parameters
        ----------
        other : Interval, int or float
            Value to be checked if it's in the interval.

        Raises
        ------
        TypeError
            If other is neither Interval, int nor float.

        Returns
        -------
        bool
            If this value is inside the interval, but not on the boundries.

        """
        if isinstance(other, Interval):
            return self.left < other.left < other.right < self.right
        elif isinstance(other, int) or isinstance(other, float):
            return self.left < other < self.right
        else:
            raise TypeError(f"Interval may only be subtracted with Interval, float or int; not {type(other)}")
    
    def __pow__(self, n):
        """
        Evaluates the Interval to the power of n,
        based on some rules provided

        Parameters
        ----------
        n : int, float

        Returns
        -------
        Interval

        """
        # We are given 1 option for odd n
        if n >= 1 and (n % 2) != 0:
            return Interval(self.left**n, self.right**n)
        # and 3 for even n
        elif n > 0 and (n % 2) == 0:
            # a >= 0
            if self.left >= 0:
                return Interval(self.left**n, self.right**n)
            # b < 0
            elif self.right < 0:
                return Interval(self.right**n, self.left**n)
            # otherwise
            else:
                return Interval(0, max([self.left**n, self.right**n]))    
        else:
            return ValueError(f"Power not defined for Interval {self} and/or {n}")
        
    def __repr__(self):
         return str([self.left, self.right])
     

"""
Tests

"""
        
I1 = Interval(1, 4)
I2 = Interval(-2, -1)
print(f"I1 + I2 == {I1 + I2} and should be [-1, 3]")        
print(f"I1 - I2 == {I1 - I2} and should be [2, 6]")        
print(f"I1 * I2 == {I1 * I2} and should be [-8, -1]")        
print(f"I1 / I2 == {I1 / I2} and should be [-4, -0.5]")

# These are my own
I3 = Interval(2,3)
print(f"Does {I1} contain {I3}: {I3 in I1}")
print(f"Does {I3} contain {I1}: {I1 in I3}")
print(f"Interval(1) should print [1, 1] and prints {Interval(1)}")

# Back to task 8
print(f"Interval(2,3) + 1 == {Interval(2,3) + 1}, should be [3, 4] ")        
print(f"1 + Interval(2,3) == {1 + Interval(2,3)}, should be [3, 4]")
print(f"Interval(2,3) + 1.0 == {Interval(2,3) + 1.0}, should be [3.0, 4.0] ")        
print(f"1.0 + Interval(2,3) == {1.0 + Interval(2,3)}, should be [3.0, 4.0]")
print(f"Interval(2,3) - 1 == {Interval(2,3) - 1}, should be [1, 2] ")        
print(f"1 - Interval(2,3) == {1 - Interval(2,3)}, should be [-2, -1]")
print(f"Interval(2,3) - 1.0 == {Interval(2,3) - 1.0}, should be [1.0, 2.0] ")        
print(f"1.0 - Interval(2,3) == {1.0 - Interval(2,3)}, should be [-2.0, -1.0]")
print(f"Interval(2,3) * 1 == {Interval(2,3) * 1}, should be [2, 3]")
print(f"1 * Interval(2,3) == {1 * Interval(2,3)}, should be [2, 3]")
print(f"Interval(2,3) * 1.0 == {Interval(2,3) * 1.0}, should be [2.0, 3.0]")
print(f"1.0 * Interval(2,3) == {1.0 * Interval(2,3)}, should be [2.0, 3.0]")

# Task 9 tests
x = Interval(-2, 2)
print(f"x**2 == {x**2}, should be [0, 4]")
print(f"x**3 == {x**3}, should be [-8, 8]")  

"""
Task 10

"""

xl = linspace(0.,1,1000)
xu = linspace(0.,1,1000)+0.5

I_list = []
  
# We create our intervals to be used as
# parameters for our polynomial
for i in range(0, len(xl)):
    I_list.append(Interval(xl[i], xu[i]))

p = lambda I: 3*I**3 - 2*I**2 - 5*I - 1

pI_list = []

# Our resulting intervals out
for I in I_list:
    pI_list.append(p(I))

yl = []
yu = []

# Getting upper and lower for all p(I)
for pI in pI_list:
    yl.append(pI.left)
    yu.append(pI.right)
    
# Plotting everything
ax = subplot()

upper_line = ax.plot(xl, yu, "b-", label="Upper limit")
lower_line = ax.plot(xl, yl, "r-", label="Lower limit")
ax.set_title(r"$p(I)=3I^3-2I^2-5I-1$, $I=[x, x+0.5]$")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$p(x)$")    
ax.legend()    
        
        
        
        
        
        
        
        