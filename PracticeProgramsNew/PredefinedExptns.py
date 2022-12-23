#3.Write a python program to demonstrate different kinds of predefined exceptions.


# exception ArithmeticError
# This class is the base class for those built-in exceptions that are raised for various arithmetic errors such as :
# OverflowError
# ZeroDivisionError
# FloatingPointError


#ZeroDivisionError or ArithmeticError:

# try:
#     a=int(input("ENter Numerator:"))
#     b=int(input("ENter Denominator:"))
#     result=a/b
#     print(result)
#
# except ZeroDivisionError:
#     print("Cannot divide by zero")

#--------------************--------------------------------

# exception LookupError
# This is the base class for those exceptions that are raised when a key or index used on a mapping or sequence is invalid or not found. The exceptions raised are :
# KeyError
# IndexError


#IndexError
#
# l=[1,2,3,4]
# try:
#     ele=int(input("Enter index to get the value frm the list:"))
#     print(l[ele])
# except IndexError:
#     print("Index not found in the list")


#--------------************--------------------------------

#Keyerror

sport = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]

ppl_play = {"hockey": 4, "soccer": 10, "football": 15, "tennis": 8}

for x in sport:
    try:
        print(ppl_play[x])
    except KeyError:
        print("Sport not found")
        # ppl_play[x] = 1


#LookupError
try:
    l=[1,2,3]
    print(l[4])
except LookupError:
    print("Index out of range")


#--------------************--------------------------------



#ValueError
# A ValueError is raised when a built-in operation or function receives an argument that has the right type but an invalid value.
try:
    print(int('a'))
except ValueError:
    print("Invalid")


#--------------************--------------------------------


# UnboundLocalError in Python occurs when variable is identified as Local but it is used prior of creation.

var=10
try:
  def func():
    #print(var)  ->identified as Local but it is used prior of creation
    var="Hello" # This causes UnboundLocalError
    print(var)
except UnboundLocalError:
    print("Unboundlocalerror")
func()



#TypeError
# TypeError is raised when an operation or function is applied to an object of inappropriate type. This exception returns a string giving details about the type mismatch.
try:
 arr = ('ab',) + 'string'
 print (arr)
except TypeError as err:
    print("Inappropriate Operation",err)

#SyntaxError
try:
    print(eval('geeks for geeks'))
except SyntaxError as err:
    print(err)




