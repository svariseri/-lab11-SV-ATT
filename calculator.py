"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def square_root(a):
    try:
        if a > 0:
            c=math.sqrt(a)
            return c
        else:
            raise ValueError
    except ValueError:
        raise ValueError

def hypotenuse(a,b):
    return math.hypot(a,b)

def add(a, b): return a+b
def sub (a,b): return a-b
def mul(a,b): return a*b
def div(a,b):
    try:
        if a!=0:
            c=b/a
            return c
        else:
            raise ZeroDivisionError
    except ZeroDivisionError:
        raise ZeroDivisionError


def log (a,b):
    try:
        c=math.log(b,a)
        return c
    except ValueError:
        raise ValueError
def exp(a,b):
    return a**b





