#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code may be used freely for any purpose,
as long as this comment is included

Created on Tue Jun 30 16:44:15 2020

@author: Emil Jonathan Eriksson
@author_email: eje1999@gmail.com
"""
from numpy import *
from matplotlib.pyplot import *
import sys
from scipy.linalg import norm, eig

"""
Task 1

"""

def is_symmetric(A):
    At = A.T
    
    if A.all() == At.all():
        return 1
    elif A.all() == -At.all():
        return -1
    else:
        return 0

A = array([[1, 7, 3],
          [7, 4, -5],
          [3, -5, 6]])

print(f"{str(A)} is symmetric, does the function work: {is_symmetric(A) == 1}")


"""
Task 2

"""

def is_orthogonal(A, B):
    """
    Checks if arrays A and B are orthogonal

    Parameters
    ----------
    A : array
        .
    B : array
        .

    Returns
    -------
    bool
        if A is orthogonal to B.

    """
    return (dot(A, B).all() == 0)

A = array([[1,0],
           [0, 1]])
B = array([[1, 1],
           [2, 2]])

print(f"{str(A)} and {str(B)} are orthogonal: {is_orthogonal(A, B)}")

C = array([[1, 1],
           [0, 0]])

print(f"{str(A)} and {str(C)} are orthogonal: {is_orthogonal(A, C)}")


"""
Task 3

"""

def my_norm(X):
    """
    Returns the norm of X, poorly

    Parameters
    ----------
    X : array
        Array to be normed.

    Returns
    -------
    x / ||x||

    """
    
    # Disclaimer: My linalg is very rusty
    factor_x = sqrt(X[0]**2 + X[1]**2)
    return float(factor_x)

C = array([[5],
           [1]])
print(f"Norm of A from SciPy: {norm(C)}, for my_norm: {my_norm(C)}")


"""
Task 4

"""

make_rot_matrix = lambda a: array([[cos(a), sin(a)], [-sin(a), cos(a)]])

def test_rotation_matrix(a_arr, tol=1.e-15):
    """
    

    Parameters
    ----------
    a_rr : list(float)
        values of angle.
    tol : float
        tolerance to be considered equal to identity matrix

    Returns
    -------
    None.

    """
    
    for a in a_arr:
        rm = make_rot_matrix(a)
        if (rm @ rm.T).all() == (rm.T @ rm).all():
            if abs(subtract((rm @ rm.T), identity(2))).all() > tol:
                print(f"False for {a}!")
            else:
                print(f"True for {a}")
        else:
            print(f"False for {a}!")

a_arr = linspace(0, 2 * pi, num=300)
test_rotation_matrix(a_arr)


"""
Task 5

"""

v = 4 * identity(20)
b = ones(19)
fill_diagonal(v[1:], b) # I loaned this coad from the &¤"()=!¤"& python mailing list
fill_diagonal(v[:,1:], b)

eigenvalues = eig(v)


"""
Task 6

"""

v2 = 4 * identity(20)
b = ones(19)
fill_diagonal(v2[1:], -b)
fill_diagonal(v2[:,1:], b)

eigenvalues2 = eig(v)