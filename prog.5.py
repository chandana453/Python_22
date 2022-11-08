# Question 5
# Level 1
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints:
# Use __init__ method to construct some parameters
#
# solution:
class inputoutputstring(object):
    def __init__(self):
        self.s = ""
    def getstring(self):
        self.s = input()
    def printstring(self):
          print (self.s.upper())
strobj=inputoutputstring()
strobj.getstring()
strobj.printstring()


