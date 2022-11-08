

# Question:86
# Please write a program to shuffle and print the list [3,6,7,8].
# Hints:
# Use shuffle() function to shuffle a list.
# Solution:
# from random import shuffle
# li = [3,6,7,8]
# shuffle(li)
# print (li)

# Question:87
# Please write a program to generate all sentences where subject is in
# ["I", "You"] and verb is in ["Play", "Love"] and the object is in
# ["Hockey","Football"].
# Hints:
# Use list[index] notation to get a element from a list.
# Solution:
# subjects=["I", "You"]
# verbs=["Play", "Love"]
# objects=["Hockey","Football"]
# for i in range(len(subjects)):
#     for j in range(len(verbs)):
#         for k in range(len(objects)):
#             sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
#             print (sentence)

# question:88
# Please write a program to print the list after removing delete even
# numbers in [5,6,77,45,22,12,24].
# Hints:
# Use list comprehension to delete a bunch of element from a list.
# Solution:
# li = [5,6,77,45,22,12,24]
# li = [x for x in li if x%2!=0]
# print(li)

# Question:89
# By using list comprehension, please write a program to print the list
# after removing delete numbers which are divisible by 5 and 7 in
# [12,24,35,70,88,120,155].
# Hints:
# Use list comprehension to delete a bunch of element from a list.
# Solution:
# li = [12,24,35,70,88,120,155]
# li = [x for x in li if x%5!=0 and x%7!=0]
# print(li)

# Question:90
# By using list comprehension, please write a program to print the list
# after removing the 0th, 2nd, 4th,6th numbers in
# [12,24,35,70,88,120,155].
# Hints:
# Use list comprehension to delete a bunch of element from a list.
# Use enumerate() to get (index, value) tuple.
# Solution:
# li = [12,24,35,70,88,120,155]
# li = [x for (i,x) in enumerate(li) if i%2!=0]
# print(li)


# Question:91
# By using list comprehension, please write a program generate a 3*5*8
# 3D array whose each element is 0.
# Hints:
# Use list comprehension to make an array.
# Solution
# array = [[[0 for co in range(8)]for col in range(5)]for row in range(3)]
# print(array)


# Question:92
# By using list comprehension, please write a program to print the list
# after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
# Hints:
# Use list comprehension to delete a bunch of element from a list.
# Use enumerate() to get (index, value) tuple.
# Solution:
# li = [12,24,35,70,88,120,155]
# li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
# print(li)

# question:93
# By using list comprehension, please write a program to print the list
# after removing the value 24 in [12,24,35,24,88,120,155].
# Hints:
# Use list's remove method to delete a value.
# Solution:
# li = [12,24,35,24,88,120,155]
# li = [x for x in li if x!=24]
# print(li)

# Question:94
# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
# write a program to make a list whose elements are intersection of the
# above given lists.
# Hints:
# Use set() and "&=" to do set intersection operation.
# Solution:
# set1=set([1,3,6,78,35,55])
# set2=set([12,24,35,24,88,120,155])
# set1 &= set2
# li=list(set1)
# print(li)

# question:95
# With a given list [12,24,35,24,88,120,155,88,120,155], write a program
# to print this list after removing all duplicate values with original
# order reserved.
# Hints:
# Use set() to store a number of values without duplicate.
# Solution:
# def removeDuplicate(li):
#     newli=[]
#     seen = set()
#     for item in li:
#         if item not in seen:
#             seen.add(item)
#             newli.append(item)
#     return newli
# li=[12,24,35,24,88,120,155,88,120,155]
# print(removeDuplicate(li))

# Question:96
# Define a class Person and its two child classes: Male and Female. All
# classes have a method "getGender" which can print "Male" for Male
# class and "Female" for Female class.
# Hints:
# Use Subclass(Parentclass) to define a child class.
# Solution:
# class person(object):
#     def getGender( self ):
#         return "Unknown"
# class Male( person ):
#     def getGender( self ):
#         return "Male"
# class Female( person ):
#     def getgender( self ):
#         return"Female"
# aMale = Male()
# aFemale = Female()
# print (aMale.getGender())
# print (aFemale.getGender())


# Question:97
# Please write a program which count and print the numbers of each
# character in a string input by console.
# Example:
# If the following string is given as input to the program:
# abcdefgabc
# Then, the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1
# Hints:
# Use dict to store key/value pairs.
# Solution:
# dic = {}
# s=input(109303890)
# for s in s:
#  dic[s] = dic.get(s,0)+1
# print ('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))

# Question:98
# Please write a program which accepts a string from console and print
# it in reverse order.
# Example:
# If the following string is given as input to the program:
# rise to vote sir
# Then, the output of the program should be:
# ris etov ot esir
# Hints:
# Use list[::-1] to iterate a list in a reverse order.
# Solution:
# s=input(8738096)
# s = s[::-1]
# print(s)


# Question:99
# Please write a program which accepts a string from console and print
# the characters that have even indexes.
# Example:
# If the following string is given as input to the program:
# H1e2l3l4o5w6o7r8l9d
# Then, the output of the program should be:
# Helloworld
# Hints:
# Use list[::2] to iterate a list by step 2.
# Solution:
# s=input(98839032)
# s = s[::2]
# print(s)

# Question:100
# Please write a program which prints all permutations of [1,2,3]
# Hints:
# Use itertools.permutations() to get permutations of list.
# Solution:
# import itertools
# print (list(itertools.permutations([1,2,3])))

# Question:100
# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a
# farm. How many rabbits and how many chickens do we have?
# Hint:
# Use for loop to iterate all possible solutions.
# Solution:
# def solve(numheads,numlegs):
#      ns='No solutions!'
#      for i in range(numheads+1):
#          j = numheads - i
#          if 2 * i + 4 * j == numlegs:
#               return i, j
#               return ns, ns
# numheads = 35
# numlegs = 94
# solutions=solve(numheads, numlegs)
# print(solutions)

