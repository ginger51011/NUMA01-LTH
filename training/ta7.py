#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code may be used freely for any purpose,
as long as this comment is included

Created on Tue Jun 30 19:18:17 2020

@author: Emil Jonathan Eriksson
@author_email: eje1999@gmail.com
"""
from numpy import *
from matplotlib.pyplot import *
import sys

class ComplexNumber():
    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            r, i = other.real, other.imag
        elif isinstance(other, int):
            r, i = other, 0
        return ComplexNumber(self.real + r, self.imag + i)
    
    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            r, i = other.real, other.imag
        elif isinstance(other, int):
            r, i = other, 0
        return ComplexNumber(self.real * r - self.imag * i, self.real * i + self.imag * r )
   
    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            r, i = other.real, other.imag
        elif isinstance(other, int):
            r, i = other, 0
        return ComplexNumber(self.real - r, self.imag - i)
    
    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            r, i = other.real, other.imag
        elif isinstance(other, int):
            r, i = other, 0
            
        # Lesgoooooooooo
        
        # (c + jd)(c - jd) == c² - d²
        n = r**2 - i**2
        
        # (a + jb)(c - jd) == ac - jad + jbc + bd
        return ComplexNumber((self.real * r + self.imag * i) / n, (self.real * i + self.imag * r) / n)
    
    def __pow__(self, n):
        # Whyyyyyyyyyyy
        r = 0
        i = 0
        # (a+ib)^n == a^n+jba^(n-1)+(jb)^2*a^(n-2)...+(jb)^n
        for m in range(0, 2*n + 1):
            # If the j cancel out
            if m % 2 == 0 and m % 4 != 0:
                r -= self.real**(n-m) * self.imag**m
            elif m % 2 == 0 and m % 4 == 0:
                r += self.real**(n-m) * self.imag**m
            elif m % 2 != 0 and n % 3 != 0 :
                i -= self.real**(n-m) * self.imag**m
            elif m % 2 != 0 and n % 3 != 0 :
                i += self.real**(n-m) * self.imag**m
            
        return ComplexNumber(r, i)
    
    def get_real(self):
        return self.real
    
    def get_imag(self):
        return self.imag
    
    def is_imaginary():
        if self.real == 0 and self.imag != 0:
            return True
        else:
            return False
    
    def is_real():
        return self.imag == 0
    
    def __repr__(self):
        return str(self.real) + " + j" + str(self.imag)
    
    def argument(self):
        a = self.real
        b = self.imag
        
        # Based on wikipedia definition
        if a > 0:
            return arctan(b / a)
        elif b >= 0 and a < 0:
            return arctan(b / a) + pi
        elif b < 0 and a < 0:
            return arctan(b / a) - pi
        elif b > 0 and a == 0:
            return pi / 2
        elif b < 0 and a == 0:
            return -pi / 2
        else:
            raise ValueError("Argument of 0+j0 not defined")
    def absolute_value(self):
        return sqrt(self.real**2 + self.imag**2)

    def __eq__(self, other):
        return (self.real == other.real and self.imag == other.imag)
    
    def add_float(self, fl):
        return ComplexNumber(float(self.real) + fl, self.imag)


"""
Tests

"""

z = ComplexNumber(1, 4)
w = ComplexNumber(2, 3)

print(f"z = {z}, w = {w}")
print(f"z + w = {z + w}")
print(f"z - w = {z - w}")
print(f"z * w = {z * w}")
print(f"z^2 = {z**2}")
print(f"z / w = {z / w}")
print(f"arg(z) = {z.argument()}")
print(f"abs(z) = {z.absolute_value()}")
print(f"Is z equal to w: {z == w}")
print(f"z + 1.1 = {z.add_float(1.1)}")











