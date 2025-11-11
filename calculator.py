"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def square_root(a):
    try:
        c=math.sqrt(a)
        return c
    except ValueError:
        print(ValueError)

def hypotenuse(a,b):
    return math.hypoth(a,b)

def add(a, b): return a+b
def sub (a,b): return a-b
def mul(a,b): return a*b
def div (a,b):
    try:
        c=b/a
        return c
    except ZeroDivisionError:
        print(ZeroDivisionError)
def log (a,b):
    try:
        c=math.log(b,a)
        return c
    except ValueError:
        print(ValueError)
def exp(a,b):
    return a**b





