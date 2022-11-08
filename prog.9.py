# Question 9
# Level 2
# Question£º
# Write a program that accepts sequence of lines as input and prints the
# lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Solution:
# lines = []
# while True:
#  s = input(10000)
# if s:
#  lines.append(s.upper())
# else:
#     "break";
# for sentence in lines:
#  print(sentence)

 # Question
 # 10
 # Level
 # 2
 # Question:
 # Write
 # a
 # program
 # that
 # accepts
 # a
 # sequence
 # of
 # whitespace
 # separated
 # words
 # as input and prints
 # the
 # words
 # after
 # removing
 # all
 # duplicate
 # words and
 # sorting
 # them
 # alphanumerically.
 # Suppose
 # the
 # following
 # input is supplied
 # to
 # the
 # program:
 # hello
 # world and practice
 # makes
 # perfect and hello
 # world
 # again
 # Then, the
 # output
 # should
 # be:
 # again and hello
 # makes
 # perfect practice world
 # Hints:
 # In
 # case
 # of
 # input
 # data
 # being
 # supplied
 # to
 # the
 # question, it
 # should
 # be
 # assumed
 # to
 # be
 # a
 # console
 # input.
 # We
 # use
 # set
 # container
 # to
 # remove
 # duplicated
 # data
 # automatically and then
 # use
 # sorted()
 # to
 # sort
 # the
 # data.
 # Solution:
# s = input(10000)
# words = [word for word in s.split(" ")]
# print(" ".join(sorted(list(set(words)))))


# Question 11
# Level 2
# Question:
# Write a program which accepts a sequence of comma separated 4 digit
# binary numbers as its input and then check whether they are divisible
# by 5 or not. The numbers that are divisible by 5 are to be printed in
# a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Solution:
# value = []
# items=[x for x in input().split(',')]
# for p in items:
#  intp = int(p, 2)
#  if not intp%5:
#     value.append(p)
# print (',').join(value)

# Question 12
# Level 2
# Question:
# Write a program, which will find all such numbers between 1000 and
# 3000 (both included) such that each digit of the number is an even
# number.
# The numbers obtained should be printed in a comma-separated sequence
# on a single line.
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Solution:
values = []
# for i in range(1000, 3001):
#  s = str(i)
#  if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and(int(s[3])%2==0):
#     values.append(s)
# print(",".join(values))

# Question 13
# Level 2
# Question:
# Write a program that accepts a sentence and calculate the number of
# letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Solution:
# s = input(10000)
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#        d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"] += 1
#     else:
#        pass
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])

# Question 14
# Level 2
# Question:
# Write a program that accepts a sentence and calculate the number of
# upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Solution:
# s = input(123)
# d={"UPPER CASE":0, "LOWER CASE":0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"]+=1
#     elif c.islower():
#        d["LOWER CASE"]+=1
#     else:
#        pass
# print ("UPPER CASE", d["UPPER CASE"])
# print ("LOWER CASE", d["LOWER CASE"])

# Question 15
# Level 2
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given
# digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Solution:
# a = input(123456789)
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# print (n1+n2+n3+n4)

# Question 16
# Level 2
# Question:
# Use a list comprehension to square each odd number in a list. The list
# is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Solution:
# values = input(12345678)
# numbers = [x for x in values.split(",") if int(x)%2!=0]
# print (",".join(numbers))

# Question 17
# Level 2
# Question:
# Write a program that computes the net amount of a bank account based a
# transaction log from console input. The transaction log format is
# shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Solution:
# netAmount = 0
# while True:
#     s = input(1900)
#     if not s:
#        break
#     values = s.split(" ")
#     operation = values[0]
#     amount = int(values[1])
#     if operation == "D":
#         netAmount += amount
#     elif operation == "W":
#         netAmount -= amount
#     else:
#         pass
# print("netAmount")
#

# Question 18
# Level 3
# Question:
# A website requires the users to input username and password to
# register. Write a program to check the validity of password input by
# users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and
# will check them according to the above criteria. Passwords that match
# the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Solutions:
# import re
# value = []
# items=[x for x in input(10099).split(',')]
# for p in items:
#     if len(p)<6 or len(p)>12:
#          continue
#     else:
#        pass
#     if not re.search("[a-z]",p):
#        continue
#     elif not re.search("[0-9]",p):
#        continue
#     elif not re.search("[A-Z]",p):
#        continue
#     elif not re.search("[$#@]",p):
#        continue
#     elif re.search("\s",p):
#        continue
#     else:
#         pass
#     value.append(p)
# print (",".join(value))

# Question 19
# Level 3
# Question:
# You are required to write a program to sort the (name, age, height)
# tuples by ascending order where name is string, age and height are
# numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'),
# ('Json', '21', '85'), ('Tom', '19', '80')]
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# We use itemgetter to enable multiple sort keys.
# Solutions:
# from operator import itemgetter, attrgetter
# l = []
# while True:
#  s = input(12345678)
#  if not s:
#      break
#  l.append(tuple(s.split(",")))
# print (sorted(l, key=itemgetter(0,1,2)))

# Question 20
# Level 3
# Question:
# Define a class with a generator which can iterate the numbers, which
# are divisible by 7, between a given range 0 and n.
# Hints:
# Consider use yield
# Solution:
# def putNumbers(n):
#     i = 0
#     while i<n:
#         j=i
#         i=i+1
#     if j%7==0:
#      yield j
# for i in "reverse",(100):
#     print(i)

# Question 21
# Level 3
# Question£º
# A robot moves in a plane starting from the original point (0,0). The
# robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The
# trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡
# The numbers after the direction are steps. Please write a program to
# compute the distance from current position after a sequence of
# movement and original point. If the distance is a float, then just
# print the nearest(integer)
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Solution:
# import math
# pos = [0,0]
# while True:
#     s = input(10000000)
#     if not s:
#          break
#     movement = s.split(" ")
#     direction = movement[0]
#     steps = int(movement[1])
#     if direction=="UP":
#        pos[0]+=steps
#     elif direction=="DOWN":
#        pos[0] -= steps
#     elif direction == "LEFT":
#        pos[1] -= steps
#     elif direction == "RIGHT":
#        pos[1] += steps
#     else:
#        pass
# print (int(round(math.sqrt(pos[1]**2+pos[0]**2))))

# Question 22
# Level 3
# Question:
# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2
# or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
# Hints
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Solution:
# freq = {} # frequency of words in text
# line = input(100209)
# for word in line.split():
#     freq[word] = freq.get(word, 0) + 1
# words = freq.keys()
# words.sort()
# for w in words:
#         print("%s:%d" % (w, freq[w]))

# Question 23
# level 1
# Question:
#  Write a method which can calculate square value of number
# Hints:
#  Using the ** operator
# Solution:
# def square(num):
#     return num ** 2
# print (square(2))
# print (square(3))

# Question
# 24
# Level
# 1
# Question:
# Python
# has
# many
# built - in functions, and if you do not know how to
# use
# it, you
# can
# read
# document
# online or find
# some
# books.But
# Python
# has
# a
# built - in document
# Solution:
# print (abs).__doc__
# print (int).__doc__
# print (input).__doc__
# def square(num):
#     '''Return the square value of the input number.
#
#      The input number must be integer.
#      '''
#     return num ** 2
# print (square(2))
# print (square.__doc__)

# Question 25
# Level 1
# Question:
# Define a class, which have a class parameter and have a same
# instance parameter.
# Hints:
#  Define a instance parameter, need add it in __init__ method
#  You can init a object with construct parameter or set the value
# later
# Solution:
# class Person:
#     # Define the class parameter "name"
#     name = "Person"

#     def __init__(self, name=None):
#
#         # self.name is the instance parameter
#         self.name = name
# jeffrey = Person("Jeffrey")
# print("%s name is %s" % (Person.name, jeffrey.name))
# nico = Person()
# nico.name = "Nico"
# print("%s name is %s" % (Person.name, nico.name))

# Question:26
# Define a function which can compute the sum of two numbers.
# Hints:
# Define a function with two numbers as arguments. You can compute the
# sum in the function and return the value.
# Solution
# def SumFunction(number1, number2):
#          return number1+number2
# print (SumFunction(1,2))

# Question:27
# Define a function that can convert a integer into a string and print
# it in console.
# Hints:
# Use str() to convert a number to string.
# Solution
# def printValue(n):
#      print(str(n))
# printValue(3)

# Question:28
# Define a function that can convert a integer into a string and print
# it in console.
# Hints:
# Use str() to convert a number to string.
# Solution
# def printValue(n):
#     print(str(n))
#     printValue(3)

# Question:29
# Define a function that can receive two integral numbers in string form
# and compute their sum and then print it in console.
# Hints:
# Use int() to convert a string to integer.
# Solution
# def printValue(s1,s2):
#          print (int(s1)+int(s2))
# printValue("3","4") #7

# Question:30
# Define a function that can accept two strings as input and concatenate
# them and then print it in console.
# Hints:
# Use + to concatenate the strings
# def printValue(s1,s2):
#     print(s1 + s2)
#     printValue("3", "4")  # 34

# Question:31
# Define a function that can accept two strings as input and print the
# string with maximum length in console. If two strings have the same
# length, then the function should print al l strings line by line.
# Hints:
# Use len() function to get the length of a string
# Solution
# def printValue(s1,s2):
#     len1 = len(s1)
#     len2 = len(s2)
#     if len1 > len2:
#         print(s1)
#     elif len2 > len1:
#         print(s2)
#     else:
#         print(s1)
#     print(s2)
#     printValue("one", "three")

# Question:32
# Define a function that can accept an integer number as input and print
# the "It is an even number" if the number is even, otherwise print "It
# is an odd number".
# Hints:
# Use % operator to check if a number is even or odd.
# Solution
# def checkValue(n):
#         if n%2 == 0:
#                 print("It is an even number")
#         else:
#                 print("It is an odd number")
# checkValue(7)

# Question:33
# Define a function which can print a dictionary where the keys are
# numbers between 1 and 3 (both included) and the values are square of
# keys.
# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Solution
# def printDict():
#         d = dict()
#         d[1] = 1
#         d[2] = 2 ** 2
#         d[3] = 3 ** 2
#         print(d)
# printDict()

# Question:34
# Define a function which can print a dictionary where the keys are
# numbers between 1 and 20 (both included) and the values are square of
# keys.
# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
#     Solution


# def printDict():
#         d = dict()
#
#
#         for i in range(1, 21):
#                  d[i] = i ** 2
#         print (d)
# printDict()

# Question:35
# Define a function which can generate a dictionary where the keys are
# numbers between 1 and 20 (both included) and the values are square of
# keys. The function should just print the values only.
# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
#     Use
#     keys()
#     to
#     iterate
#     keys in the
#     dictionary.Also
#     we
#     can
#     use
#     item()
#     to
#     get
#     key / value
#     pairs.
#     Solution


# def printDict():
#         d = dict()
#
#
#         for i in range(1, 21):
#                 d[i] = i ** 2
#         for (k, v) in d.items():
#                     print (v)
# printDict()

# Question:36
# Define a function which can generate a dictionary where the keys are
# numbers between 1 and 20 (both included) and the values are square of
# keys. The function should just print the keys only.
# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item()
# to get key/value pairs.
# Solution:

# def printDict():
#          d=dict()
#          for i in range(1,21):
#                 d[i]=i**2
#          for k in d.keys():
#                print (k)
# printDict()

# Question:37
# Define a function which can generate and print a list where the values
# are square of numbers between 1 and 20 (both included).
# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
#     Use
#     list.append()
#     to
#     add
#     values
#     into
#     a
#     list.
# Solution:
# def printList():
#         li = list()
#         for i in range(1, 21):
#                 li.append(i ** 2)
#         print(li)
# printList()

# Question:38
# Define a function which can generate a list where the values are
# square of numbers between 1 and 20 (both included). Then the function
# needs to print the first 5 elements in the list.
# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
#     Use
#     list.append()
#     to
#     add
#     values
#     into
#     a
#     list.
#     Use[n1:n2]
#     to
#     slice
#     a
#     list
# Solution:
# def printList():
#          li=list()
#          for i in range(1,21):
#                 li.append(i**2)
#          print (li[:5])
# printList()

# Question:39
# Define a function which can generate a list where the values are
# square of numbers between 1 and 20 (both included). Then the function
# needs to print the first 5 elements in the list.
# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list
# Solution
# def printList():
#        li=list()
#        for i in range(1,21):
#               li.append(i**2)
#        print (li[:5])
# printList()

# Question:40
# Define a function which can generate a list where the values are
# square of numbers between 1 and 20 (both included). Then the function
# needs to print the last 5 elements in the list.
# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list
# Solution
# def printList():
#         li=list()
#         for i in range(1,21):
#                 li.append(i**2)
#         print (li[-5:])
# printList()

# Question:41
# Define a function which can generate a list where the values are
# square of numbers between 1 and 20 (both included). Then the function
# needs to print all values except the first 5 elements in the list.
# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list
# Solution
# def printList():
#          li = list()
#          for i in range(1, 21):
#                  li.append(i ** 2)
#          print(li[5:])
# printList()

# Question:42
# Define a function which can generate and print a tuple where the value
# are square of numbers between 1 and 20 (both included).
# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
#     Use
#     list.append()
#     to
#     add
#     values
#     into
#     a
#     list.
#     Use
#     tuple()
#     to
#     get
#     a
#     tuple
#     from a list.
# Solution
# def printTuple():
#         li = list()
#         for i in range(1, 21):
#             li.append(i ** 2)
#         print(tuple(li))
#         li=list()
#         for i in range(1,21):
#                 li.append(i**2)
#         print (tuple(li))
# printTuple()

# question:43
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print
# the first half values in one line and the last half values in one
# line.
# Hints:
# Use [n1:n2] notation to get a slice from a tuple.
# Solution
# tp=(1,2,3,4,5,6,7,8,9,10)
# tp1=tp[:5]
# tp2=tp[5:]
# print (tp1)
# print (tp2)

# Question:44
# Write a program to generate and print another tuple whose values are
# even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
# Hints:
# Use "for" to iterate the tuple
# Use tuple() to generate a tuple from a list.
# Solution

# li=list()
# for i in "tp":
#         if "tp"[i]%2==0:
#                 li.append("tp"[i])
# tp2=tuple(li)
# print (tp2)

# Question:45
# Write a program which accepts a string as input to print "Yes" if the
# string is "yes" or "YES" or "Yes", otherwise print "No".
# Hints:
# Use if statement to judge condition.
# Solution
# s= input(100000)
# if s=="yes" or s=="YES" or s=="Yes":
#  print ("Yes")
# else:
#  print ("No")

# Question:46
# Write a program which can filter even numbers in a list by using
# filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
# Hints:
# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.
# Solution
# li = [1,2,3,4,5,6,7,8,9,10]
# evenNumbers = filter(lambda x: x%2==0, li)
# print (evenNumbers)

