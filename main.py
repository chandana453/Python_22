# ############ D A T A   S T R U C T U R E S ###############
# """Data Structures are a way of organizing data so that it can be
#  accessed more efficiently depending upon the situation."""
# list = [1,2,3,"hi",2.2]
# print(list)
# #lisr accessing (0 to N-1) and in reverse (-1 to -N)
#
# dict = {
#     "name": "harshith",
#     "age": 23
# }
#
# print(dict["age"])
# print(dict.get("name"))
# print(dict.keys())
# print(dict.items())
#
#
# s = (1,2,"hi",3,"hello","hello")
# print(set(s))
#
#
# """LINKED LIST"""
# #A linked list is a linear data structure, in which the elements
# # are not stored at contiguous memory locations. The elements in
# # a linked list are linked using pointers.
#
# import copy

# class node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class linked_list:
#     def __init__(self):
#         self.head = None
#
#     def print_list(self):
#         temp = self.head
#         while (temp):
#             print(temp.data)
#             temp = temp.next
#
#
#
# list = linked_list()
# list.head = node("1")
# e2 = node("2")
#
#
# list.head.next = e2
# list.print_list()


#
# class node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class linked_list:
#     def __init__(self):
#         self.head = None
#
#     def print_list(self):
#         temp = self.head
#         while temp:
#             print(temp.data)
#             temp = temp.next
#
#
# list = linked_list()
# list.head = node("1")
# e2 = node("2")
# e3 = node("3")
#
#
# list.head.next = e2
# e2.next = e3
#
#
# list.print_list()



#
#
# new_list = [i for i in range(20) if i %2 ==0 ]
# print(new_list)
#
# dict ={
#     "name": "harshith",
#     "age": 23,
#     "work": "kalli"
# }
# new_dict = { key : value for (key,value) in dict.items() if dict["name"] == "harshith" }
# print(new_dict)




#
#
#
# import copy
#
# l1 = [ 1,2,3,[4,5],6]
# l2 = copy.copy(l1)
# l2.append(2)
# l1[3][0]=2
#
#
# print(l1,l2)
# print(id(l1))
# print(id(l2))


#
# is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
# print(is_even_list.pop())
#
# # iterate on each lambda function
# # and invoke the function to get the calculated value
# for i in is_even_list:
#     print(i())

# import array as arr
# import numpy as np
#
# b = np.array([[1,2],[3,4]])
# tup = (1,2,3)
# a = np.array(tup)
# print(b)
# print(a)
#
# # a = arr.array([1,2,3])
# #
# # for i in a:
# #     print(i)



#work hours on all dates as input as int arr
#produce pay amont as output
# pay = hours * pre type rate
#if sat or sun pre type rate = 2.0



# hours_per_day = [9,0,2,0,0,3,9]
# le = len(hours_per_day)
#
# def pay_amount(hours):
#     sum = 0
#
#     for item in hours:
#         if item == hours[5]:
#             break
#         sum += item
#         if item > 8:#premium type
#             print(item * 2.0)
#         elif item == 8:
#             print(item * 1.0)
#         if sum == 30:
#             return sum *1.5
#
#     end_sum = 0
#     for i in hours[5:7]:
#         end_sum += i
#
#     print(end_sum)
#     return end_sum * 2.0
#
# print(pay_amount(hours_per_day))

#
# s = input("enter a string :")
# b = []
# def cap(s):
#     a = s.split(" ")
#     for i in a:
#         b.append(i.capitalize())
#     print(" ".join(b))
#
#
# cap(s)

# print(s.title())


# s = [1,2,3]
# # x = [lambda arg=x : arg*10 for x in s]
# #
# # for i in x:
# #     print(i())
# x = list(map(lambda s : s * 10,s))
# print(x)
# print((map(lambda s : s * 10,s)))
#
# l =[1,2,3,4]
# k =[]
# for i in l:
#     k.append(i)
#
# print(k)


#Python Program to Find Largest Number in a List
# l = [1,2,3,4,5,3]
# l.sort()
# print(l)
# print(l[-1])
# print(max(l))

#Python Program to Find Second Largest Number in a List
# l = [1,2,3,4,5,3]
# l.sort()
# print(l[-2])

#
#Python Program to Print Largest Even and Largest Odd Number in a List
# l=[2,3,4,5,6]
# curr_eve = 0
# curr_odd = 0
# for num in l:
#     if num%2 ==0 and num > curr_eve:
#         curr_eve = num
#     elif num % 2 ==1 and num > curr_odd:
#         curr_odd = num
# print(curr_eve, curr_odd)

#Python Program to Split Even and Odd Elements into Two Lists
# l = [2,3,4,5]
# eve_list = []
# odd_list = []
# for num in l:
#     if num%2 ==0:
#         eve_list.append(num)
#     elif num % 2 != 0:
#         odd_list.append(num)
#
# print(eve_list,odd_list)


#Python Program to Find Average of a List
# l = [1,2,3,4,5]
# le = len(l)
# sum = sum(l)
# avg = sum/le
# print(avg)


#Python Program to Print Sum of Negative Numbers, Positive Even & Odd Numbers in a List
# l = [-2,-5,-7,3,6,7,4]
# neg_list = []
# pos_list = []
# for num in l:
#     if num < 0:
#         neg_list.append(num)
#     elif num >= 0:
#         pos_list.append(num)
#
# print(sum(neg_list),sum(pos_list))

#Python Program to Count Occurrences of Element in List
# l=[1,2,2,3,3,4,4,4,4,4]
# print(l.count(4))

#Python Program to Find the Sum of Elements in a List using Recursion
# def sum(mylist):
#     if len(mylist) == 1:  # last element termination condition
#         return mylist[0]
#     else:
#         return mylist[0] + sum(mylist[1:])
#
#
# k = [1, 6, 5, 7, 3]
# print(sum(k))

#Python Program to Merge Two Lists and Sort it
# l = [1,2,5,6,9]
# k=[2,4,5,8]
# l.extend(k)
# print(l)
# l.sort()
# print(l)


#Python Program to Remove Duplicates from a List

# l = [1,1,2,2,3,3,4,4,5,5]
# print(list(set(l)))


#Python Program to Swap the First and Last Element in a List
# l = [1,2,3,4,5]
# l[0],l[4] = l[4],l[0]
# print(l)


#Python Program to Sort a List According to the Second Element in Sublist

# def Sort(sub_li):
#     l = len(sub_li)
#     for i in range(0, l):
#         for j in range(0, l - i - 1):
#             if (sub_li[j][1] > sub_li[j + 1][1]):
#                 tempo = sub_li[j]
#                 sub_li[j] = sub_li[j + 1]
#                 sub_li[j + 1] = tempo
#     return sub_li
#
#
# # Driver Code
# sub_li = [['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]
# print(Sort(sub_li))

#Python Program to Return the Length of the Longest Word from the List of Words
# def find(l):
#     max = 0
#     temp = 0
#     for item in l:
#         if len(item)> max:
#             max = len(item)
#             temp = item
#
#     return temp
#
# l=["hi","bye","heheheh","hello"]
# print(find(l))
#


#Python Program to Find the Number Occurring Odd Number of Times in a List
# def odd_times(list):
#
#     l = len(list)
#     for i in range(l):
#         count = 0
#         for j in range(0,l):
#             if list[j]==list[i]:
#                 count+=1
#
#         if count%2 !=0:
#             return i
#
#
# arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2 ]
# print(odd_times(arr))


#Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List
# import random
#
# l = []
# a = random.randint(1,20)
# l.append(a)
# print(l)

#Python Program to Find the Cumulative Sum of a List
# l=[1,2,3,4,5]
# k=[]
# cu= 0
# for i in range(len(l)):
#     cu+=l[i]
#     k.append(cu)
# print(k)


#Python Program to Find the Union of Two Lists
# l = [1,2,3,4,5]
# k=[5,6,7,8,9]
# print(l+k)

#Python Program to Find the Intersection of Two Lists
# l=[1,2,3,4,5]
# k=[5,6,7,8,3]
# list = [value for value in l if value in k]
# print(list)



# #Python Program to Check if a String is a Pangram or Not
# l ="kik"
# k=l[::-1]
# if l == k :
#     print("blah")



#Python Program to Remove the nth Index Character from a Non-Empty String
# str="harshith is my name"
# n=4
# str=str.replace("h","$")
# st = str.replace(" ","-")
# print(str)
# print(st)



#Python Program to Reverse a String Without using Recursion
# str="harshith is my name"
# a=str.split(" ")
# b=[]
# for i in a[::-1]:
#     b.append(i)
#
# print(" ".join(b))


#Python Program to Determine How Many Times a Given Letter Occurs in a String
# str="harshith is my name"
# print(str.count("a"))

#Python Program to Find the Length of a String without Library Function
# str ="hello"
# count=0
# for i in str:
#     count+=1
# print(count)



#Python Program to Count the Number of Vowels in a String
# str="harshith is my name"
# l=["a","e","i","o","u"]
# count=0
# for i in str:
#     if i in l:
#         count+=1
# print(count)

#
# d = {
#     "name": "harshith",
#     "age": 23,
#     "place": "nellore",
# }

# Python Program to Check if a Key Exists in a Dictionary or Not
# if "name" in d.keys():
#     print("ok")


# Python Program to Add a Key-Value Pair to the Dictionary
# d.update({"year":1999})
# print(d)


# Python Program to Find the Sum of All the Items in a Dictionary

# dict = {'a': 100, 'b': 200, 'c': 300}
# print(sum(list(dict.values())))



# Python Program to Multiply All the Items in a Dictionary

# dict = {'a': 1, 'b': 2, 'c': 3}
# mul=1
# for i in dict.values():
#     mul*=i
# print(mul)

# Python Program to Remove a Key from a Dictionary
# # print(d.popitem())
# del d["name"]
# print(d)


# Python Program to Concatenate Two Dictionaries
#
# dict = {'a': 1, 'b': 2, 'c': 3}
# d.update(dict)
# print(d)

# Python Program to Map Two Lists into a Dictionary
# l=["me","u"]
# k=[1,2]
# print(dict(zip(l,k)))

# Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character

# Python Program to Create Dictionary that Contains Number
# n =4
# d={}
# for i in range(n):
#     d.update({i:i*i})
#     # d[i]=i*i
# print(d)

# Python Program to Count the Frequency of Each Word in a String using Dictionary
# str ="my name is harshith"
# a = str.split(" ")
# d ={}
# for i in a:
#     l = len(i)
#     d.update({i:l})
#
# print(d)




#
# #calculator for n vales
#
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
#
# operations = {
#     '+': add,
#     '-': sub,
#     '*': mul,
#     '/': div
# }
#
#
# def calculator():
#     # print(logo)
#     game_is = True
#     a = float(input("What's the first number?"))
#
#     while game_is:
#         b =  float(input("What's the second number?"))
#         print("availablee operations are +,-,*,/")
#         op = input("enter operation to perform")
#
#
#         ans = operations[op](a,b)
#         print(ans)
#         ask = input("if u wanna continue type yes or no to close:").upper()
#         if ask =="YES":
#            a = ans
#
#         else:
#             game_is = False
#
#
# calculator()
#




# def calculate(op,a,b):
#
#     if op =="add":
#         return a+b
#     if op =="sub":
#         return a-b
#     if op=="mul":
#         return a*b
#     if op=="div":ff
#         return a/b
#
# a=int(input("enter first value: "))
# game_is =True
# while game_is:
#     print("operations available are add, sub,mul,div")
#     op = input("enter operation to perform: ").lower()
#
#     b=int(input("enter second number: "))
#
#     ans = calculate(op,a,b)
#     print(ans)
#
#     ask = input("if u wanna continue type yes or no to stop: ").upper()
#
#     if ask == "YES":
#         a=ans
#     else:
#         game_is = False


#
# def name(initial):
#     print("hi")
#     def age():
#         print("22")
#         return initial()
#     return age()
#
# @name
# def initial():
#     print("challa")

# var = 0
# def update():
#     global var
#     var = 3
#     print(var)
#
# update()
# print(var)

# global_var = 0
# def modify_global_var():
#     global global_var # Setting global_var as a global variable
#     global_var = 10
#     print(global_var)
# def printing_global_var():
#     print(global_var) # There is no need to declare global variable
# modify_global_var()
# printing_global_var() # Prints 10
# print(global_var)



# n =1234
# reverse = 0
# while n > 0:
#     re = n % 10
#     reverse = reverse * 10+ re
#     print(reverse)
#     n  = n // 10
#     print(n)
#
# print(reverse)



