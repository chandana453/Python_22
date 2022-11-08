'''Write a program which will find all such numbers which are divisible
by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence
on a single line.
Hints:
Consider use range(#begin, #end) method'''

'''l=[]
for i in range(2000,3200):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
print(','.join(l))'''
'''Write a program that calculates and prints the value according to the
given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a
comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to
the program:
100,150,180
The output of the program should be:
18,22,24
Hints:
If the output received is in decimal form, it should be rounded off to
its nearest value (for example, if the output received is 26.0, it
should be printed as 26)
In case of input data being supplied to the question, it should be
assumed to be a console input.
import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(math.sqrt(2*c*float(d)/h))))
print(','.join(value))'''
'''num=int(input('enter a num:'))
if(num%2==0):
    if(num%4==0):
        print('it is even')
else:
    print('it is odd')'''
'''Please write a program which accepts a string from console and print
the characters that have even indexes.
Example:
If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:
Helloworld
Hints:
Use list[::2] to iterate a list by step 2.'''
'''a='h1e2l3l4o5w6o7r8l9d'
a=a[::2]
print(a)'''
'''a='i am fine
a=a[::-1]
print(a)'''
'''b=('am mandala chabitey kada')
b=b[::-1]
print(b)'''
# Program on itertools permutations
'''from itertools import permutations
permu=permutations([1, 2, 3, 4],2)
for i in list(permu):
      print(i)'''
'''dic = {}
s='abcdefgabc'
for i in s:
 count =s.count(i)
 dic[i]=count'''
#for k in dic.keys():
 #print(k)
#print(dic.items())
'''for k,v in dic.items():
 print(k,v)'''
#print(dic)
'''Define a class Person and its two child classes: Male and Female. All
classes have a method "getGender" which can print "Male" for Male
class and "Female" for Female class.
Hints:
Use Subclass(Parentclass) to define a child class.'''

'''class person(object):
    def getGender(self):
        return "unknown"

class male(person):
    def getGender(self):
        return "male"

# class female(person):
#     def getGender(self):
#         return "female"
# 
# amale=male()
# afemale=female()'''
'''With a given integral number n, write a program to generate a
dictionary that contains (i, i*i) such that is an integral number
between 1 and n (both included). and then the program should print the
dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.
Consider use dict()'''
'''n=int(input())
d=dict()
for i in range(1,n+1):
 d[i] = i*i
print(d)'''
'''Write a program which accepts a sequence of comma-separated numbers
from console and generate a list and a tuple which contains every
number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.
tuple() method can convert list to tuple'''
'''a=input()
l=a.split()
t=tuple(l)
print(l)
print(t)'''
'''Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
Hints:
Use __init__ method to construct some parameters'''
'''class InputOutString(object):
 def __init__(self):
     self.s = ""
 def getString(self):
     self.s = input()
 def printString(self):
     print(self.s.upper())
strObj = InputOutString()
strObj.getString()
strObj.printString()'''
#(or)
#by using program convert lower case into upper case
'''a='dayam'
print(a.upper())'''
'''Write a program that calculates and prints the value according to the
given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a
comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to
the program:
100,150,180
The output of the program should be:
18,22,24
Hints:
If the output received is in decimal form, it should be rounded off to
its nearest value (for example, if the output received is 26.0, it
should be printed as 26)
In case of input data being supplied to the question, it should be
assumed to be a console input. '''
'''import math 
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(value))'''
# import random
# p=(1,2,3,4,5,6,7,8,9)
# l=[]
# for i in p:
#     l.append(i)
# print(l)
'''Write a program which takes 2 digits, X,Y as input and generates a 2-
dimensional array. The element value in the i-th row and j-th column
of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
Hints:
Note: In case of input data being supplied to the question, it should
be assumed to be a console input in a comma-separated form.'''
# input_str = input()
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# for row in range(rowNum):
#  for col in range(colNum):
#      multilist[row][col]= row*col
# print(multilist)
'''Write a program that accepts a comma separated sequence of words as
input and prints the words in a comma-separated sequence after sorting
them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.'''
# a=[x for x in input().split(',')]
# a.sort()
# print(','.join(a))
'''Write a program that accepts sequence of lines as input and prints the
lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.'''
# lines = []
# while True:
#  s = input()
#  if s:
#      lines.append(s.upper())
#  else:
#      break;
# for i in lines:
#     print(i)
'''Write a program that accepts a sequence of whitespace separated words
as input and prints the words after removing all duplicate words and
sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.
We use set container to remove duplicated data automatically and then
use sorted() to sort the data.'''
# a=input()
# h=[x for x in a.split(" ")]
# print(''.join(sorted(list(set(h))
'''Write a program which accepts a sequence of comma separated 4 digit
binary numbers as its input and then check whether they are divisible
by 5 or not. The numbers that are divisible by 5 are to be printed in
a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.'''
# i = []
# x=[x for x in input().split(',')]
# for p in x:
#  intp = int(p, 2)
#  if not intp%5:
#     i.append(p)
# print(','.join(i))
'''Write a program, which will find all such numbers between 1000 and
3000 (both included) such that each digit of the number is an even
number.
The numbers obtained should be printed in a comma-separated sequence
on a single line.
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.'''
# h = []
# for i in range(1000, 3001):
#  s = str(i)
#  if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and(int(s[3])%2==0):
#             h.append(s)
# print(",".join(h))
'''Write a program that accepts a sentence and calculate the number of
letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.'''
# s = input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#   if c.isdigit():
#     d["DIGITS"]+=1
#   elif c.isalpha():
#       d["LETTERS"]+=1
#   else:
#     pass
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])
'''Write a program that accepts a sentence and calculate the number of
upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.'''
# s = input()
# d={"UPPER CASE":0, "LOWER CASE":0}
# for c in s:
#  if c.isupper():
#    d["UPPER CASE"]+=1
#  elif c.islower():
#    d["LOWER CASE"]+=1
#  else:
#      pass
# print("UPPER CASE", d["UPPER CASE"])
# print("LOWER CASE", d["LOWER CASE"])
'''Write a program that computes the value of a+aa+aaa+aaaa with a given
digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.'''
# a = input()
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# print(n1+n2+n3+n4)
'''Use a list comprehension to square each odd number in a list. The list
is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.'''
# values = input()
# numbers = [x for x in values.split(",") if int(x)%2!=0]
# print(",".join(numbers))
'''Write a program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is
shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.'''
# netAmount = 0
# while True:
#  s = input()
#  if not s:
#   break
#  values = s.split(" ")
#  operation = values[0]
#  amount = int(values[1])
#  if operation=="D":
#     netAmount+=amount
#  elif operation=="W":
#     netAmount-=amount
#  else:
#     pass
# print(netAmount)
'''A website requires the users to input username and password to
register. Write a program to check the validity of password input by
users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and
will check them according to the above criteria. Passwords that match
the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.'''
# import re
# value = []
# items=[x for x in input().split(',')]
# for p in items:
#  if len(p)<6 or len(p)>12:
#   continue
#  else:
#    pass
#  if not re.search("[a-z]",p):
#    continue
#  elif not re.search("[0-9]",p):
#    continue
#  elif not re.search("[A-Z]",p):
#    continue
#  elif not re.search("[$#@]",p):
#    continue
#  elif re.search("\s",p):
#    continue
#  else:
#   pass
#  value.append(p)
# print(",".join(value))
'''You are required to write a program to sort the (name, age, height)
tuples by ascending order where name is string, age and height are
numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'),
('Json', '21', '85'), ('Tom', '19', '80')]
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.
We use itemgetter to enable multiple sort keys.'''
# from operator import itemgetter, attrgetter
# l = []
# while True:
#  s = input()
#  if not s:
#   break
#  l.append(tuple(s.split(",")))
# print(sorted(l, key=itemgetter(0,1,2))
'''A robot moves in a plane starting from the original point (0,0). The
robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The
trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡
The numbers after the direction are steps. Please write a program to
compute the distance from current position after a sequence of
movement and original point. If the distance is a float, then just
print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.'''
# import math
# pos = [0,0]
# while True:
#  s = input()
#  if not s:
#   break
#  movement = s.split(" ")
#  direction = movement[0]
#  steps = int(movement[1])
#  if direction=="UP":
#   pos[0]+=steps
#  elif direction=="DOWN":
#   pos[0]-=steps
#  elif direction=="LEFT":
#   pos[1]-=steps
#  elif direction=="RIGHT":
#   pos[1]+=steps
#  else:
#    pass
# print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
'''Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2
or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
Hints
In case of input data being supplied to the question, it should be
assumed to be a console input.'''
# freq = {} # frequency of words in text
# line = input()
# for word in line.split():
#    freq[word] = freq.get(word,0)+1
# word = freq.keys()
# word.sort()
# for w in word:
#  print("%s:%d" % (w,freq[w]))
# Write a method which can calculate square value of number
# Hints:
#  Using the ** operator
# def square(num):
#    return num ** 2
# print(square(2))
# print(square(3))
'''Python
has
many
built - in functions, and if you do not know how to
use
it, you
can
read
document
online or find
some
books.But
Python
has
a
built - in document
function
for every built - in functions.
    Please
    write
    a
    program
    to
    print
    some
    Python
    built - in functions
documents, such as abs(), int(), raw_input()
And
add
document
for your own function

Hints:
The
built - in document
method is __doc__'''
# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)
# def square(num):
#     '''Return the square value of the input number.
#
#     The input number must be integer.
#     '''
#     return num ** 2
#
#
# print(square(2))
# print(square.__doc__)
'''Define a class, which have a class parameter and have a same
instance parameter.
Hints:
 Define a instance parameter, need add it in __init__ method
 You can init a object with construct parameter or set the value
later'''
# # Define the class parameter "name"
# name = "Person"
# def __init__(self, name=None):
# # self.name is the instance parameter
#   self.name =name
#  jeffrey = Person("Jeffrey")
# print("%s name is %s" % (Person.name, jeffrey.name)nico = Person()nico.name = "Nico")
# print("%s name is %s" % (Person.name, nico.name))
'''Define a function which can compute the sum of two numbers.
Hints:
Define a function with two numbers as arguments. You can compute the
sum in the function and return the value.'''
# def SumFunction(number1, number2):
#  return number1+number2
# print(SumFunction(1,2))
'''it in console.
Hints:
Use str() to convert a number to string.'''
# def printValue(n):
#  print(str(n))
# printValue(3)
'''Define a function that can convert a integer into a string and print
it in console.
Hints:
Use str() to convert a number to string.'''
# def printValue(n):
#  print(str(n))
# printValue(3)
'''Define a function that can receive two integral numbers in string form
and compute their sum and then print it in console.
Hints:
Use int() to convert a string to integer.'''
# def printValue(s1,s2):
#  print(int(s1)+int(s2))
# printValue("3","4") #7
'''Define a function that can accept two strings as input and concatenate
them and then print it in console.
Hints:
Use + to concatenate the strings'''
# def printValue(s1,s2):
#  print(s1+s2)
# printValue("3","4") #34
'''Define a function that can accept two strings as input and print the
string with maximum length in console. If two strings have the same
length, then the function should print al l strings line by line.
Hints:
Use len() function to get the length of a string'''
# def printValue(s1,s2):
#   len1 = len(s1)
#   len2 = len(s2)
#   if len1>len2:
#         print(s1)
#   elif len2>len1:
#           print(s2)
#   else:
#       print(s1)
#       print(s2)
# printValue("one","three")
'''Define a function that can accept an integer number as input and print
the "It is an even number" if the number is even, otherwise print "It
is an odd number".
Hints:
Use % operator to check if a number is even or odd.'''
# def checkValue(n):
#      if n%2 == 0:
#           print("It is an even number")
#      else:
#           print("It is an odd number")
# checkValue(7)
'''Define a function which can print a dictionary where the keys are
numbers between 1 and 3 (both included) and the values are square of
keys.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.'''
# def printDict():
#    d=dict()
#    d[1]=1
#    d[2]=2**2
#    d[3]=3**2
#    print(d)
'''printDictDefine a function which can print a dictionary where the keys are
numbers between 1 and 20 (both included) and the values are square of
keys.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
'''
# def printDict():
#     d = dict()
#     for i in range(1, 21):
#            d[i] = i ** 2
#     print(d)
# printDict()
'''Define a function which can generate a dictionary where the keys are
numbers between 1 and 20 (both included) and the values are square of
keys. The function should just print the values only.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item()
to get key/value pairs.'''

# def printDict():
#   d=dict()
#   for i in range(1,21):
#     d[i]=i**2
#   for (k,v) in d.items():
#      print(v)
# printDict()
'''Define a function which can generate a dictionary where the keys are
numbers between 1 and 20 (both included) and the values are square of
keys. The function should just print the keys only.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item()
to get key/value pairs.'''
# def printDict():
#    d=dict()
#    for i in range(1,21):
#         d[i]=i**2
#    for k in d.keys():
#     print(k)
# printDict()
'''Define a function which can generate and print a list where the values
are square of numbers between 1 and 20 (both included).
Hints:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.'''
# def printList():
#   li=list()
#   for i in range(1,21):
#    li.append(i**2)
#   print(li)
# printList()
''''Define a function which can generate a list where the values are
square of numbers between 1 and 20 (both included). Then the function
needs to print the last 5 elements in the list.
Hints:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list'''
# def printList():
#   li=list()
#   for i in range(1,21):
#          li.append(i**2)
#   print(li[-5:])
# printList()

'''Define a function which can generate a list where the values are
square of numbers between 1 and 20 (both included). Then the function
needs to print the first 5 elements in the list.
Hints:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list'''
# def printList():
#       li=list()
#       for i in range(1,21):
#        li.append(i**2)
#       print(li[:5])
# printList()
'''Define a function which can generate a list where the values are
square of numbers between 1 and 20 (both included). Then the function
needs to print all values except the first 5 elements in the list.
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list'''
# def printList():
#        li=list()
#        for i in range(1,21):
#             li.append(i**2)
#        print(li[5:])
# printList()
'''With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print
the first half values in one line and the last half values in one
line. 
Hints:
Use [n1:n2] notation to get a slice from a tuple.'''
# tp=(1,2,3,4,5,6,7,8,9,10)
# tp1=tp[:5]
# tp2=tp[5:]
# print(tp1)
# print(tp2)
'''Write a program to generate and print another tuple whose values are
even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
Hints:
Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list.'''
tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
    if tp[i]%2==0:
         li.append(tp[i])
tp2=tuple(li)
print(tp2)
























































