#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code may be used freely for any purpose,
as long as this comment is included

Created on Thu Jul  2 09:23:48 2020

@author: Emil Jonathan Eriksson
@author_email: eje1999@gmail.com
"""
from numpy import *
from matplotlib.pyplot import *
import sys

"""
Task 1

"""

class PolyGon():
    
    def __init__(self, cpoints):
        self._cpoints = cpoints
        self._edges = []
        for i in range(0, len(cpoints)):
            if i < len(cpoints) - 1:
                self._edges.append(cpoints[i+1] - cpoints[i])
            else:
                self._edges.append(cpoints[-1] - cpoints[0])
    
    def plot(self, line_color="orange"):
        # I am uncertain how one would use the _edges attribute
        # to do this...
        for i in range(0, len(self._cpoints)):
            if i < len(self._cpoints) - 1:
                plot(self._cpoints[i], self._cpoints[i+1], color=line_color)
            else:
                plot(self._cpoints[-1], self._cpoints[0], color=line_color)
                
    def get_points(self):
        return self._cpoints

cpoints = [array([0,0]), array([1,0]), array([1,1]), array([1,0])]
pg = PolyGon(cpoints)
pg.plot()


"""
Task 2

"""

class Rectangle(PolyGon):
    
    def __init__(self, cpoints):
        if len(cpoints) != 4:
            raise ValueError(f"A rectangle has 4 corners, you entered {len(cpoints)}")
        PolyGon.__init__(self, cpoints)
        
    def area(self):
        
        # We use the cross product for area
        return abs(cross(self._edges[0], self._edges[1]))

r = Rectangle(cpoints)
figure()
r.plot(line_color="red")
print(f"Area of the rectangle is {r.area()} a.u.")


"""
Task 3

"""

class SpecialRectangle(Rectangle):
    
    def __init__(self, cpoints):
        Rectangle.__init__(self, cpoints)
        
        # We use the dot product to decide if
        # the sides are parallel to the axes
        x_base = [1, 0]
        y_base = [0, 1]
        
        # We don't know in which order the edges come, must test both
        if dot(self._edges[0], y_base) == 0 and dot(self._edges[1], x_base) == 0:
           pass
        elif dot(self._edges[0], x_base) == 0 and dot(self._edges[1], y_base) == 0:
            pass
        else:
            raise ValueError("SpecialRectangle must have sides parallel to the axes")
    
    def __contains__(self, B):
        a_point_list = self.get_points()
        for b_point in B.get_points():
            
            # x-axis check
            b_x = b_point[0]
            # Since points next to eachother share x or y-value,
            # we only check opposites (diagonals)
            a_x1 = a_point_list[0][0]
            a_x2 = a_point_list[2][0]
            print(f"{a_x1}, {b_x}, {a_x2}")
        
            # a_x1 might be to the right or the left of a_x2; 
            # We check both possibillities
            if not a_x1 < b_x < a_x2 and not a_x2 < b_x < a_x1:
                return False
            
            # y-axis check
            b_y = b_point[1]
            a_y1 = a_point_list[0][1]
            a_y2 = a_point_list[2][1]
            
            if not a_y1 < b_x < a_y2 and not a_y2 < b_x < a_y1:
                return False
        else:
            return True

A = SpecialRectangle(cpoints)
b_cpoints = [array([0.25,0.25]), array([0.25,0.75]), array([0.75,0.75]), array([0.75,0.25])]
B = SpecialRectangle(b_cpoints)

figure()
A.plot()
B.plot(line_color="red")
title(f"Is B in A: {B in A}")




