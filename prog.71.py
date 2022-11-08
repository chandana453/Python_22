# Question:71
# Please write assert statements to verify that every number in the list
# [2,4,6,8] is even.
# Hints:
# Use "assert expression" to make assetion.
# Solution:
# li = [2,4,6,8]
# for i in li:
#        assert i%2==0

# Question:72
# Please write a program which accepts basic mathematic expression from
# console and print the evaluation result.
# Example:
# If the following string is given as input to the program:
# 35+3
# Then, the output of the program should be:
# 38
# Hints:
# Use eval() to evaluate an expression.
# Solution:
# expression = input(2098675889)
# print (eval(expression))

# Question:73
# Please write a binary search function which searches an item in a
# sorted list. The function should return the index of element to be
# searched in the list.
# Hints:
# Use if/elif to deal with conditions.
# Solution:
# import math
# def bin_search(li,element):
#     bottom = 0
#     top = len(li)-1
#     index = -1
#     while top>=bottom and index==1:
#         mid = int(math.floor((top+bottom)/2.0))
#         if li[mid]==element:
#             index = mid
#         elif li[mid]>element:
#             top = mid-1
#         else:
#             bottom = mid+1
#             return index
#         li-[2,5,7,9,11,17,222]
#         print (bin_search(li,11))
#         print (bin_search(li,12))

# Question:74
# Please write a binary search function which searches an item in a
# sorted list. The function should return the index of element to be
# searched in the list.
# Hints:
# solution:
#  import math
#  def bin_search(li, element):
#      bottom = 0
#      top = len(li)-1
#      index = -1
#      while top>=bottom and index==-1:
#           mid = int(math.floor((top+bottom)/2.0))
#           if li[mid]==element:
#               index = mid
#      elif li[mid]>element:
#           top = mid-1
#      else:
#         bottom = mid+1
#   return index
# li=[2,5,7,9,11,17,222]
# print (bin_search(li.11))
# print (bin_search(li,12))

# Question:75
# Please generate a random float where the value is between 10 and 100
# using Python math module.
# Hints:
# Use random.random() to generate a random float in [0,1].
# Solution:
# import random
# print(random.random()*100)

# Question:76
# Please generate a random float where the value is between 5 and 95
# using Python math module.
# Hints:
# Use random.random() to generate a random float in [0,1].
# Solution:
# import random
# print(random.random()*100-5)

# Question:77
# # Please write a program to output a random even number between 0 and 10
# # inclusive using random module and list comprehension.
# # Hints:
# # Use random.choice() to a random element from a list.
# # Solution:
# import random
# print (random.choice([i for i in range(11)if i%2==0]))

# Question:78
# Please write a program to output a random number, which is divisible
# by 5 and 7, between 0 and 10 inclusive using random module and list
# comprehension.
# Hints:
# Use random.choice() to a random element from a list.
# Solution:
# import random
# print (random.choice([i for i in range(201) if i%5==0and i%7]))

# Question:79
# Please write a program to generate a list with 5 random numbers
# between 100 and 200 inclusive.
# Hints:
# Use random.sample() to generate a list of random values.
# Solution:
#import random

# Question:80
# Please write a program to randomly generate a list with 5 even numbers
# between 100 and 200 inclusive.
# Hints:
# Use random.sample() to generate a list of random values.
# Solution:
# import random
# print (random.sample([i for i in range(100,201) if i%2--0],5))

# Question:81
# Please write a program to randomly generate a list with 5 numbers,
# which are divisible by 5 and 7 , between 1 and 1000 inclusive.
# Hints:
# Use random.sample() to generate a list of random values.
# Solution
# import random
# print (random.sample([i for i in range(1,1001) if i%5==0 and i%7==0],5))


# Question:82
# Please write a program to randomly print a integer number between 7
# and 15 inclusive.
# Hints:
# Use random.randrange() to a random integer in a given range.
# Solution:
# import random
# print (random.randrange(7,16))

# Question:83
# Please write a program to compress and decompress the string "hello
# world!hello world!hello world!hello world!".
# Hints:
# Use zlib.compress() and zlib.decompress() to compress and decompress a
# string.
# Solution:
# import zlib
# s = 'hello world!hello world!hello world!hello world!'
# t = zlib.compress(s)
# print (t)
# print (zlib.decompress(t))

# Question:84
# Please write a program to print the running time of execution of "1+1"
# for 100 times.
# Hints:
# Use timeit() function to measure the running time.
# Solution:
# from timeit import Timer
# t = Timer("for i in range(100):1+1")
# print (t.timeit())

# Question:85
# Please write a program to shuffle and print the list [3,6,7,8].
# Hints:
# Use shuffle() function to shuffle a list.
# Solution:
# from random import shuffle
# li = [3,6,7,8]
# shuffle(li)
# print (li)
