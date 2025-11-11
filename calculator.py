"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): return a+b
def sub (a,b): return a-b
def mul(a,b): return a*b

def log (a,b):
    try:
        c=math.log(b,a)
        return c
    except ValueError:
        print(ValueError)
def exp(a,b):
    return a**b





