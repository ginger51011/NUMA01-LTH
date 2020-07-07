#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code may be used freely for any purpose,
as long as this comment is included

Created on Tue Jul  7 11:19:34 2020

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
        if isinstance(other, Interval):
            return Interval(self.left + other.left, self.right + other.right)
        elif isinstance(other, int) or isinstance(other, float):
            return Interval(self.left + other, self.right + other)
        else:
            raise ValueError(f"Interval may only be added to Interval, float or int; not {type(other)}")
    
    def __sub__(self, other):
        if isinstance(other, Interval):
            return Interval(self.left - other.right, self.right - other.left)
        elif isinstance(other, int) or isinstance(other, float):
            return Interval(self.left - other, self.right - other)
        else:
            raise ValueError(f"Interval may only be subtracted with Interval, float or int; not {type(other)}")
    
    def __mul__(self, other):
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
            raise ValueError(f"Interval may only be multiplicated with Interval, float or int; not {type(other)}")
        
    def __truediv__(self, other):
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
            raise ValueError(f"Interval may only be multiplicated with Interval, float or int; not {type(other)}")
    
    def __contains__(self, other):
        if isinstance(other, Interval):
            return self.left < other.left < other.right < self.right
        elif isinstance(other, int) or isinstance(other, float):
            return self.left < other < self.right
        else:
            raise ValueError(f"Interval may only be subtracted with Interval, float or int; not {type(other)}")
    
    def __pow__(self, n):
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

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        