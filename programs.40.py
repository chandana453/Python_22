# 1) Write a program to print the following into a text file.
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# solution:
# file1 = open("myfile.txt","w")
# L = ["This is Delhi \n","This is paris \n","This is london \n"]
# file1.write("Hello \n")
# file1.writelines(L)
# file1.close()
# file1 = open("myfile.txt","r+")
# print("Output of Read function is")
# print(file1.read())
# print()
# file1.seek(0)
# print( "Output of Rreadline function is ")
# print(file1.readline())
# print()
# file1.seek(0)
# print("Output of Readline(9) function is ")
# print(file1.readline())
# file1.seek(0)
# print("Output of Readlines function is ")
# print(file1.readlines())
# print()
# file1.close()
import math

# 2)Write a python program with buggy code and add a try/except clause so the code runs without errors.
# solution:
# def divide(x,y):
#     try:
#         result = x // y
#         print("Yeah ! Your answer is :", result)
#     except ZeroDivisionErrror:
#         print("sorry ! You are dividing by zero ")
# divide(3,0)

# 3)Write a python program to demonstrate different kinds of predefined exceptions.
# solution
# def fun(a):
#     if a < 4:
#         b = a/(a-3)
#         print("value of b = ", b)
#         try:
#             fun(3)
#             fun(5)
#         except ZeroDivisionError:
#             print("ZeroDivisionError Occured and Handled")
#         except NameError:
#             print("NameError Occured and Handled")

# 4)Write a python program to demonstrate user-defined exceptions.
# solution:
# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return(repr(self.value))
# try:
#     raise(MyError(3*2))
# except MyError as error:
#     print('A New Exception occured: ', error.value)


# 5)Write a Python program to demonstrate different modes of a file open method.
# solution:
# file = open('geek.txt','w')
# file.write("This is the write comand")
# file.write("It allows us to write in a particular file")
# file.close()

# 6)Write a python program to find all the longest words(which have more than 10 characters) from the file.
# solution:

# def longest_word(filename):
#     with open(filename, 'r') as infile:
#               words = infile.read().split()
#     max_len = len(max(words, key=len))
#     return [word for word in words if len(word) == max_len]
#     print(longest_word('test.txt'))

# 7)Write a Python program to count the frequency of words in a file.
# solution:
# text = open("sample.txt", "r")
# d = dict()
# for line in text:
#     line = line.strip()
#     line = line.lower()
#     words = line.split(" ")
#     for word in words:
#         if word in d:
#             d[word] = d[word] + 1
#         else:
#             d[word] = 1
# for key in list(d.keys()):
#     print(key, ":", d[keys])


# 8)Write a Python program to append 'El Niño' string to the text file using encoding.
# solution:
# file1 = open("myfile.txt", "w")
# l = ["This is Delhi \n", "This is paris \n", "This is London"]
# file1.writelines(l)
# file1.close()
# file1 = open("myfile.txt", "a")
# file1.write("Today \n")
# file1.close()
# file1 = open("myfile.txt", "r")
# print("Output of Readlines after appending")
# print()
# (file1.read())
# print()
# file1.close()
# file1 = open("myfile.txt", "w")
# file1.write("Tomorrow \n")
# file1.close()
# file1 = open("myfile.txt","r")
# print("Output of Readlines after writing")
# print(file1.read())
# print()
# file1.close()

# 9)Write a program to demonstrate modules.
# solution:
# from math import sqrt,factorial
# print(sqrt(16))
# print(factorial(6))

# 10)Write a program to use specific imports from a module to other modules.
# solution:
# import math
# pie = math.pi
# print("The value of pi is : ",pie)

# 11) Write a Python program to count the number of characters (character frequency) in a string
# Sample String: google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
# solution:
# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] +=1
#         else:
#             dict[n] = 1
#             return dict
#         print(char_frequency('google.com'))

# 12)Write a Python program to find the first appearance of the substring 'not' and 'poor' from a
# given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string.
# Sample String: 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result: 'The lyrics is good!'
# 'The lyrics is poor!'
# solution:
# def not_poor(str1):
#     snot = str1.find('not')
#     sbad = str1.find('poor')
#     if sbad > snot:
#         str1 = str1.replace(str1[snot:(sbad+4)], 'good')
#         return str1
#     print(not_poor('The lyrics is not that poor!'))


# 13)Write a Python program to sum all the items in a list using reduce.
# solution:
# def sum_list(items):
#     sum_numbers = 0
#     for x in items:
#         sum_numbers += x
#         return sum_numbers
#     print(sum_list([1,2,-8]))

# 14)Write a Python program to count the number of strings where the string length is 2 or more and the first
# and the last characters are the same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result: 2
# solution:
# def match_words(words):
#     ctr = 0
#     for word in words:
#         if len(word) > 1 and word[0] == word[-1]:
#             ctr += 1
#             return ctr
#         print(match_words(['abc', 'xyz', 'aba', '1221']))


# 15)Write a Python program to convert a list into a dictionary where keys are the unique elements of the list and the values are their frequency.
# Ex:
# Input: ['a', 'b', 'c', 'a', 'd', 'e']
# Output: {'a': 2, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
# solution:

# def Convert(a):
#     it = iter(a)
#     res_dct = dict(zip(it, it))
#     return res_dct
# lst = ['a', 1, 'b', 2, 'c', 3]
# print(Convert(lst))

# 16) Write a Python program to multiply all the items in a dictionary
# solution:
# my_dict = {'data1':100,'data2':-54,'data3':247}
# result=1
# for key in my_dict:
#     result=result * my_dict[key]
#     print(result)
#

# 17)Write a Python program to get the maximum and minimum value in a dictionary
# solution:
# my_dict = {'x':500, 'y':5874, 'z':560}
# key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
# key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
# print('Maximum value: ',my_dict[key_max])
# print('Minimum value: ',my_dict[key_min])

# 18)Read 3 numbers and print them in sorted order.
# solution:
# def sortList(lst):
#     digits = [int(digit) for digit in str(lst) ]
#     return sum(digits)
# lst = [12,10,106,31,15]
# print(sorted(lst,key = sortList))


# 19)Read two values using input() and find the first value position in the list and replace that with the second value in the list.
# solution:
# def swapPositions(list,pos1, pos2):
#     list[pos1], list[pos2] = list[pos2], list[pos1]
#     return list
# List = [23, 65, 19, 90]
# pos1, pos2, = 1,3
# print(swapPositions(List, pos1-1, pos2-1))


# 20)Define a function that will take two positional arguments and one default argument. And print sum of those arguments.
# solution:
# def greet(name, msg):
#     """This function greets to the person with the provided message"""
#     print("Hello", name + ', ' + msg)
#     greet("Monica", "Good morning!")


# 21)Define a function with dynamic arguments, keyword arguments and update the keyword arguments in a dictionary within the function.
# solution:
# def myFun(*args, **kwargs):
#     print("args: ", args)
#     print("kwargs: ", kwargs)
# args = input("Enter a args: ")
# kwargs = input("Enter kwargs: ")
# myFun(args,kwargs)

# 22)Create an Arithmetic class that has functions for addition, subtraction create one more class Calculator which have multiplication, division
#    now inherit the class Arithmetic into Calculator and access all the methods.
# solution:
# def add(num1, num2):
#     return num1 + num2
# def subtract(num1, num2):
#     return num1 - num2
# def multiply(num1, num2):
#     return num1 * num2
# def divide(num1, num2):
#     return num1 / num2
# print("Please select operation -\n" \
#       "1.Add\n" \
#       "2.Subtract\n" \
#       "3.Multiply\n" \
#       "4.Divide\n")
# select =  int(input("Select operations form 1,2,3,4, :"))
# number_1 = int(input("Enter first number: "))
# number_2 = int(input("Enter second number: "))
# if select == 1:
#     print(number_1, "+", number_2, "=",
#            add(number_1, number_2))
# elif select == 2:
#     print(number_1, "-", number_2, "=",
#           subtract(number_1, number_2))
# elif select == 3:
#     print(number_1, "*", number_2, "=",
#           multiply(number_1, number_2))
# elif select == 4:
#     print(number_1, "/", number_2, "=",
#           divide(number_1, number_2))
# else:
#     print("Invalid input")

# 23)Create a class that has a method for float division and inherit this class into the above calculator class.
# solution:
# class cal():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         def add(self):
#             return self.a+self.b
#         def mul(self):
#             return self.a*self.b
#         def div(self):
#             return self.a/self.b
#         def sub(self):
#             return self.a-self.b
#         a=int(input("Enter first number: "))
#         b=int(input("Enter second number: "))
#         obj=cal(a,b)
#         choice=1
#         while choice!=0:
#             print("0. Exit")
#             print("1. Add")
#             print("2. Subtraction")
#             print("3. Multiplication")
#             print("4. Divison")
#             choice=int(input("Enter choice: "))
#             if choice==1:
#                 print("Result: ",obj.add())
#             elif choice==2:
#                 print("Result: ",obj.sub())
#             elif choice==3:
#                 print("Result: ", obj.mul())
#             elif choice==4:
#                 print("Result: ",round(obj.div(),2))
#             elif choice==0:
#                 print("Exiting!")
#             else:
#                 print("Invalid choice!!")
#                 print()

# 24)Write a program to demonstrate multiple and multi-level inheritances by using the above-defined classes.
# solution:
# class Class1:
#     def m(self):
#         print("In Class")
# class Class2("Class1"):
#     def m(self):
#         print("In Class")
# class Class3(Class1):
#     def m(self):
#         print("In Class3")
#         class Class4(Class2, Class3):
#             pass
#         obj = Class4()
#         obj.m()

# 25)Program to create and insert data into a text file.
# solution:
# file1 = open('myfile.txt', 'w')
# L = ["This is Delhi \n", "This is paris \n" "This is London \n"]
# s = "Hello\n"
# file1.write(s)
# file1.writelines(L)
# file1.close()
# file1 = open('myfile.txt','r')
# print(file1.read())
# file1.close()


# 26)Program to append strings from the below list to the text file using encoding and also print the data.
# solution:
# import fileinput
# def main():
#     linenumber = 0
#     for line in fileinput.input():
#        line = line.rstrip()
#        lineNumber += 1
#        print('{}: {}'.format(lineNumber, line))
# if __name__ =='__main__':

# 27)Program to print data of the above text file with and without using the context manager(with)?
# solution:
# class ContextManager():
#     def __init__(self):
#         print('init method called')
#     def __enter__(self):
#             print('enter method called')
#             return self
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#             print('exit method called')
# with ContextManager() as manager:
#             print('with statement block')

# 28)Program to execute pre-defined exceptions?
# solution:
# def square_root(Number)
#     assert (Number<0),"Give a positive integer"
#     return Number**(1/2)
# print(square_root(36))
# print(square_root(-36))


# 29)Given an integer,n, perform the following conditional actions by creating two user-defined exceptions.
# If n is odd, raise Weird
# If n is even and in the inclusive range of 2 to 5, raise Not_Weird
# If n is even and in the inclusive range of 6 to 20, raise Weird
# If n is even and greater than 20, raise Not_Weird
# print weird if Weird exception raised and print not weird if Not_Weird exception
# solution:
import math
import os
import random
import re
import sys
# if __name__ == '__main__':
#     n = int(input().strip())
#     if n%2 !=0:
#         print("Weird")
#     elif n%2 == 0 and n>2 and n<=5:
#         print("Not Weird")
#     elif n%2 ==0 and n > 6 and n <=20:
#         print("Weird")
#     else:
#         print("Not Weird")

# 30)Write any example for map, filter, and reduce methods?
# solution:
# const oldArray = [1,2,3,4];
# let sum = oldArray.reduce9((accumulator,currentValue) => {
#     return accumulator + currentValue;
# },10);
# console.log(sum): // 20 ((1+2+3+4)+10)

# 31)Write a program to seggrigate list values
# Ex Input: [1,0,1,2,0,1,0,2]
# Expected Output: [0,0,0,1,1,1,2,2]
# solution:
# mylist = [1,2,3,4,5,6,7,8,9,10]
# print(mylist[1:9])
# print(mylist[1:9:2])
# print(mylist[1:9:3])

# 32)Write a program to print unique words from a file.
# solution:
# def countUniqueWords(fileName):
#     file = open(fileName, 'r')
#     read_file = file.read().lower()
#     words_in_file = read_file.split()
#     count_map = {}
#     for i in words_in_file:
#         if i in count_map:
#             count_map[i] +=1
#         else:
#             count_map[i] = 1
#             count = 0
#             for i in count_map:
#                 if count_map[i] == 1:
#                     count += 1
#                     file.close()
#                     return count
#                 with open("gfg.txt", "w") as file:
#                     file.write("Geeksforgeeks was created with\
#                                a goal in mind to provide well written well \
#                                thought and well explained solutions\
#                                for selected  quetions")
#                     print('Number of unique words in the file are:',
#                           countUniqueWords('gfg.txt'))


# 33)Write a program to create a decorator which decides whether a person is eligible for the vote or not.
# solution:
# age = int(input("Enter age : "))
# if age >= 18:
#     print("Eligible for Voting!")
# else:
#     print("Not Eligible for Voting!")

# 34)Write a program to create a decorator which updates the result param based on the percentage of a student.
# solution:
# def decorators(*args, **kwargs):
#     def inner(func):
#         '''
#            do operations with func
#            '''
#         return func
#     return inner
# @decorators()
# def func():
#      """
#          function implementation
#     """

# 35)Write a program to create a decorator which returns the factorial of a given number using reduce function.
# solution:
# def factorial(n):
#        """calculates the factorial of n,
#        n should be an integer and n <= 0"""
#        if type(n) == int and n >=0:
#            if n == 0:
#                return 1
#            else:
#                return n * factorial(n-1)
#        else:
#            raise TypeError("n has to be positive integer or zero")


# 36)Write a program to create a decorator which returns the unique words from a file to the main function.
# solution:
# def shout(text):
#     return text.upper()
# print(shout('Hello'))
# yell = shout
# print(yell('Hello'))

# 37)Write a program to raise user-defined exceptions to find if a list contains duplicates if the list contains a float number and any other two user-defined exceptions of your choice.
# solution:
# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#         def __str__(self):
#             return(repr(self.value))
#         try:
#             raise(MyError(3*2))
#         except MyError as error:
#            print('A New Exception occured: ', .value)


# 38)Write a program to print the factorial of each element in a list using multi-threading.
# solution:
# def factorial(x)
#     """This is



























































































