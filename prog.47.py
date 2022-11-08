# Question:47
# Write a program which can map() to make a list whose elements are
# square of elements in [1,2,3,4,5,6,7,8,9,10].
# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.
# Solution
# li = [1,2,3,4,5,6,7,8,9,10]
# squaredNumbers = map(lambda x: x**2, li)
# print (squaredNumbers)

# Question:48
# Write a program which can map() and filter() to make a list whose
# elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
# Hints:
# Use map() to generate a list.
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.
# Solution
# li = [1,2,3,4,5,6,7,8,9,10]
# evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
# print (evenNumbers)

# Question:49
# Write a program which can filter() to make a list whose elements are
# even number between 1 and 20 (both included).
# Hints:
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.
# Solution
# evenNumbers = filter(lambda x: x%2==0, range(1,21))
# print (evenNumbers)

# Question:50
# Write a program which can map() to make a list whose elements are
# square of numbers between 1 and 20 (both included).
# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.
# Solution
# quaredNumbers = map(lambda x: x**2, range(1,21))
# print (squaredNumbers)

# Question51
# Define a class named American which has a static method called
# printNationality.
# Hints:
# Use @staticmethod decorator to define class static method.
# Solution
# class American(object):
#       @staticmethod
#       def printNationality():
#           print ("America")
# anAmerican = American()
# anAmerican.printNationality()
# American.printNationality()

# Question:52
# Define a class named American and its subclass NewYorker.
# Hints:
# Use class Subclass(ParentClass) to define a subclass.
# Solution:
# class American(object):
#     pass
# class NewYorker(American):
#     pass
#
# anAmerican = American()
# aNewYorker = NewYorker()
# print(anAmerican)
# print(aNewYorker)

# Question:53
# Define a class named Circle which can be constructed by a radius. The
# Circle class has a method which can compute the area.
# Hints:
# Use def methodName(self) to define a method.
# Solution:
# class Circle(object):
#     def __init__(self, r):
#        self.radius = r
#     def area(self):
#         return self.radius ** 2 * 3.14
#
# aCircle = Circle(2)
# print(aCircle.area())

# question:54
# Define a class named Rectangle which can be constructed by a length
# and width. The Rectangle class has a method which can compute the
# area.
# Hints:
# Use def methodName(self) to define a method.
# Solution:
# class Rectangle(object):
#     def __init__(self, l, w):
#         self.length = l
#         self.width = w
#
#     def area(self):
#          return self.length * self.width
#
# aRectangle = Rectangle(2, 10)
# print(aRectangle.area())

# question:55
# Define a class named Shape and its subclass Square. The Square class
# has an init function which takes a length as argument. Both classes
# have a area function which can print the area of the shape where
# Shape's area is 0 by default.
# Hints:
# To override a method in super class, we can define a method with the
# same name in the super class.
# Solution:
# class Shape(object):
#     def __init__(self):
#         pass
#     def area(self):
#        return 0
# class Square(Shape):
#     def __init__(self, l):
#       Shape.__init__(self)
#       self.length = l
#     def area(self):
#        return self.length * self.length
# aSquare = Square(3)
# print(aSquare.area())

# quetion:56
# Please raise a RuntimeError exception.
# Hints:
# Use raise() to raise an exception.
# Solution:
# raise RuntimeError('something wrong')

# question:57
# Write a function to compute 5/0 and use try/except to catch the
# exceptions.
# Hints:
# Use try/except to catch exceptions.
# Solution:
# def throws():
#     return 5 / 0
# try:
#         throws()
# except ZeroDivisionError:
#      print ("division by zero!")
# finally:
#         print('In finally block for cleanup')

# question:58
# Define a custom exception class which takes a string message as
# attribute.
# Hints:
# To define a custom exception, we need to define a class inherited from
# Exception.
# Solution:
#  """My own exception class
#  Attributes:
#  msg -- explanation of the error
#  """
#  def __init__(self, msg):
#         self.msg = msg
# error = MyError("something wrong")

# Question:59
# Assuming that we have some email addresses in the
# "username@companyname.com" format, please write program to print the
# user name of a given email address. Both user names and company names
# are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# john
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Hints:
# Use \w to match letters.
# Solution:
# import re
# emailAddress = input(20)
# pat2 = "(\w+)@((\w+\.)+(com))"
# r2 = re.match(pat2,emailAddress)
# print (r2.group(1))

# Question:60
# Assuming that we have some email addresses in the
# "username@companyname.com" format, please write program to print the
# company name of a given email address. Both user names and company
# names are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# google
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Hints:
# Use \w to match letters.
# Solution:
# import re
# emailAddress = input(600)
# pat2 = "(\w+)@(\w+)\.(com)"
# r2 = re.match(pat2,emailAddress)
# print (r2.group(2))