# bad_code.py  ← intentionally bad code for agent to review
import os
import sys
password = "admin123"        # security issue!
def add(a,b):                # style issue!
    x=a+b                    # style issue!
    return x

def divide(a, b):
    return a/b               # bug! no zero division check

unused_variable = "hello"    # bug! never used