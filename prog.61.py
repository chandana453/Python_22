# Question:61
# Write a program which accepts a sequence of words separated by
# whitespace as input to print the words composed of digits only.
# Example:
# If the following words is given as input to the program:
# 2 cats and 3 dogs.
# Then, the output of the program should be:
# ['2', '3']
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Hints:
# Use re.findall() to find all substring using regex.
# Solution:
# import re
# s = input(80)
# print (re.findall("\d+",s))

# Question:62
# Print a unicode string "hello world".
# Hints:
# Use u'strings' format to define unicode string.
# Solution:
# unicodeString = u"hello world!"

# question:63
# Write a program to read an ASCII string and to convert it to a unicode
# string encoded by utf-8.
# Hints:
# Use unicode() function to convert.
# Solution:
# s = input(628)
# u = unicode( s ,"utf-8")
# print (u)

# Question:64
# Write a special comment to indicate a Python source code file is in
# unicode.
# Hints:
# Solution:
# -*- coding: utf-8 -*-

# Question:65
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input
# by console (n>0).
# Example:
# If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 3.55
# In case of input data being supplied to the question, it should be
# assumed to be a console input
# Hints:
# Use float() to convert an integer to a float
# Solution:
# n=int(input(638))
# sum=0.0
# for i in range(1,n+1):
#  sum += float(float(i)/(i+1))
# print (sum)

# question:66
# Write a program to compute:
# f(n)=f(n-1)+100 when n>0
# and f(0)=1
# with a given n input by console (n>0).
# Example:
# If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 500
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Hints:
# We can define recursive function in Python.
# Solution:
# def f(n):
#      if n==0:
#            return 0
#            return f(n-1)+100
# n=int(input(287))
# print (f(n))


# Question:67
# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n
# input by console.
# Example:
# If the following n is given as input to the program:
# 7
# Then, the output of the program should be
# 13
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Hints:
# We can define recursive function in Python.
# Solution:
# def f(n):
#  if n == 0: return 0
#  elif n == 1: return 1
#  else: return f(n-1)+f(n-2)
# n=int(input(869))
# print (f(n))

# Question:68
# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program using list comprehension to print the Fibonacci
# Sequence in comma separated form with a given n input by console.
# Example:
# If the following n is given as input to the program:
# 7
# Then, the output of the program should be:
# 0,1,1,2,3,5,8,13
# Hints:
# We can define recursive function in Python.
# Use list comprehension to generate a list from an existing list.
# Use string.join() to join a list of strings.
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Solution:
# def f(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return f(n-1)+f(n-2)
# n = int(input())
# values = [str(f(x)) for x in range(0, n + 1)]
# print(",".join(values))

# Question:69
# Please write a program using generator to print the even numbers
# between 0 and n in comma separated form while n is input by console.
# Example:
# If the following n is given as input to the program:
# 10
# Then, the output of the program should be:
# 0,2,4,6,8,10
# Hints:
# Use yield to produce the next value in generator.
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Solution:
# def EvenGenerator(n):
#     i=0
#     while i<=n:
#         if i%2==0:
#             yield i
#         i += 1
# n = int(input())
# values = []
# for i in EvenGenerator(n):
#     values.append(str(i))
# print(",".join(values))

# Question:70
# Please write a program using generator to print the numbers which can
# be divisible by 5 and 7 between 0 and n in comma separated form while
# n is input by console.
# Example:
# If the following n is given as input to the program:
# 100
# Then, the output of the program should be:
# 0,35,70
# Hints:
# Use yield to produce the next value in generator.
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Solution:
# def NumGenerator(n):
#    for i in range(n+1):
#        if i%5==0 and i%7==0:
#            yield i
# n=int(input())
# values = []
# for i in NumGenerator(n):
#     values.append(str(i))
# print(",".join(values))



