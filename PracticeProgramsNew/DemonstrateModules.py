#9.Write a program to demonstrate modules.


#A Python module is a file containing Python definitions and statements. A module can define functions, classes, and variables. A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use. It also makes the code logically organized.

#1.simple Python module

def add(a,b):
    return a+b

def sub(a,b):
    return a-b
#
# print(add(5,6))
# print(sub(10,5))

#2.import module

import calc
print(calc.add(9,7))   #calc is a module we have imported

#3.from-import Statement

from math import sqrt,factorial

print(sqrt(14))
print(factorial(4))

#4. from import *

from math import *

print(sqrt(9))

#5.List of directories-Here, sys.path is a built-in variable within the sys module. It contains a list of directories that the interpreter will search for the required module.

import sys
print(sys.path)

#6.

import math as mt
print(mt.factorial(3))




#Python built-in modules
# There are several built-in modules in Python, which you can import whenever you like.
# importing built-in module math
import math

# using square root(sqrt) function contained in math module
print(math.sqrt(25))

# using pi function contained in math module
print(math.pi)

# 2 radians = 114.59 degrees
print(math.degrees(2))

# 60 degrees = 1.04 radians
print(math.radians(60))

# Sine of 2 radians
print(math.sin(2))

# Cosine of 0.5 radians
print(math.cos(0.5))

# Tangent of 0.23 radians
print(math.tan(0.23))

# 1 * 2 * 3 * 4 = 24
print(math.factorial(4))

# importing built in module random
import random

# printing random integer between 0 and 5
print(random.randint(0, 5))

# print random floating point number between 0 and 1
print(random.random())

# random number between 0 and 100
print(random.random() * 100)

List = [1, 4, True, 800, "python", 27, "hello"]

# using choice function in random module for choosing a random element from a set such as a list
print(random.choice(List))


# importing built in module datetime
import datetime
from datetime import date
import time

# Returns the number of seconds since the Unix Epoch, January 1st 1970
print(time.time())

# Converts a number of seconds to a date object
print(date.fromtimestamp(454554))