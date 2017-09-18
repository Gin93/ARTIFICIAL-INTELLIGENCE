""" File name:   math_functions.py
    Author:      <Zi Jin u5541673 >
    Date:        <2/3/2017>
    Description: This file defines a set of variables and simple functions.
                 
                 It should be implemented for Exercise 1 of Assignment 0.
                 
                 See the assignment notes for a description of its contents.
"""
import math
from math import *
ln_e = log(e)
twenty_radians=radians(20)

def quotient_ceil (numerator,denominator):
    ''' returns the ceiling of the numerator divided by the denominator

        (number) -> int
    '''
    return ceil(numerator/denominator)

def quotient_floor (numerator,denominator):
    ''' returns the floor of the numerator divided by the denominator

        (number) -> int
    '''
    return floor(numerator/denominator)

def manhattan (x1,y1,x2,y2):
    ''' returns the Manhattan distance between the two points specified by these arguments.

        (number,number,number,number) -> number
    '''
    return (fabs(x1-x2)+fabs(y1-y2))



    
    

