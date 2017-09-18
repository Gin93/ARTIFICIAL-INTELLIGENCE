""" File name:   truth_tables.py
    Author:      <Zi Jin u5541673>
    Date:        <2/3/2017>
    Description: This file defines a number of functions which implement Boolean
                 expressions.
                 
                 It also defines a function to generate and print truth tables
                 using these functions.
                 
                 It should be implemented for Exercise 2 of Assignment 0.
                 
                 See the assignment notes for a description of its contents.
"""
def boolean_fn1(a, b, c):
    return not(a or b) or ( not a and  not b)

def boolean_fn2(a, b, c):
    return (a and b) or( not a and not b)

def boolean_fn3(a, b, c):
    return (not c or b) and (a and not b) or (not a and b)


def draw_truth_table(boolean_fn):
    """ This function prints a truth table for the given boolean function.
        It is assumed that the supplied function has three arguments.

        ((bool, bool, bool) -> bool) -> None
    """
    first_line = "a       b      c      res"
    print(first_line)
    print((len(first_line) + 2)*"-")
    print("False   False  False ",boolean_fn(False,False,False))
    print("False   False  True  ",boolean_fn(False,False,True))
    print("False   True   False ",boolean_fn(False,True,False))
    print("False   True   True  ",boolean_fn(False,True,True))
    print("True    False  False ",boolean_fn(True,False,False))
    print("True    False  True  ",boolean_fn(True,False,True))
    print("True    True   False ",boolean_fn(True,True,False))
    print("True    True   True  ",boolean_fn(True,True,True))

	
print(draw_truth_table(boolean_fn3))