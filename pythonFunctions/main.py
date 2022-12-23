# This is a sample Python script.

# 1.abs()
# The abs() function returns the absolute value of the specified number.
print("......abs......")
x = abs(-5.75)
print(x)

# 2.The all() function returns True if all items in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the all() function also returns True.
print(".....all().....")
mylist = [0, 1, 1]
x = all(mylist)
print(x)

mylist = [0, True, False]
x = all(mylist)
print(x)

mydict = {0: "Apple", 1: "Orange"}
x = all(mydict)
print(x)

# Returns False because the first key is false.

# For dictionaries the all() function checks the keys, not the values.

# 3.any()
# The any() function returns True if any item in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the any() function will return False.
print("....any().....")
mytuple = (0, 1, False)
x = any(mytuple)
print(x)

# Returns True because the second item is True

mydict = {0: "Apple", 1: "Orange"}
x = any(mydict)
print(x)

# Returns True because the second key is True.

# For dictionaries the any() function checks the keys, not the values.

# 4.ascii()
# The ascii() function returns a readable version of any object (Strings, Tuples, Lists, etc).
# The ascii() function will replace any non-ascii characters with escape characters:
# å will be replaced with \xe5.

print('.......ascii()........')
x = ascii("My name is Ståle")
print(x)

# 5.bin()
# The bin() function returns the binary version of a specified integer.
# The result will always start with the prefix 0b.
print(".........bin.....")
x = bin(36)
print(x)

print(".......bool()......")
# The bool() function returns the boolean value of a specified object.
# The object will always return True, unless:
# The object is empty, like [], (), {}
# The object is False
# The object is 0
# The object is None

x = bool(1)
print(x)

print(".....bytearray.....")
# The bytearray() function returns a bytearray object.
# It can convert objects into bytearray objects, or create empty bytearray object of the specified size.
x = bytearray(4)
print(x)

print(".....bytes()......")
# The bytes() function returns a bytes object.
# The difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified, and bytearray() returns an object that can be modified.
x = bytes(4)
print(x)

print("....callable().....")


# The callable() function returns True if the specified object is callable, otherwise it returns False.
def x():
    a = 5


print(callable(x))

a = 5
print(callable(a))

print("....chr().....")
# The chr() function returns the character that represents the specified unicode.
x = chr(102)
print(x)

print("/.....classmethod()....")
# classmethod()	Converts a method into a class method

print("....compile()......")
# The compile() function returns the specified source as a code object, ready to be executed
x = compile('print(55)', 'test', 'eval')
exec(x)
# The compile() function returns the specified source as a code object, ready to be executed.

x = compile('print(55)\nprint(88)', 'test', 'exec')
exec(x)

print(".....complex()......")
# the complex() function returns a complex number by specifying a real number and an imaginary number.
x = complex('3+5j')
print(x)

x = complex(4, 7)
print(x)

print("//////delattr().....")


# The delattr() function will delete the specified attribute from the specified object.
class Person:
    age = 36
    name = "abc"
    country = "aus"


delattr(Person, 'age')
print(Person)

x = getattr(Person, 'name')
print(x)

y = hasattr(Person, 'country')
print(y)

setattr(Person, 'name', "aaa")
k = getattr(Person, 'name')
print(k)

print(".....dict().....")
# dict() function creates a dictionary.
# A dictionary is a collection which is unordered, changeable and indexed.
x = dict(name='JOhn', age=36, country="Norway")
print(x)

print("......dir()......")


# The dir() function returns all properties and methods of the specified object, without the values.
class Person:
    name = "aaaa"
    age = 40
    country = "US"


x = dir(Person)
print(x)

print("......divmod().......")
# The divmod() function returns a tuple containing the quotient  and the remainder when argument1 (dividend) is divided by argument2 (divisor).
x = divmod(5, 2)
print(x)

print('......enumerate()........')
# enumerate() will takes a collection (tuples etc) and return it as an enumerate object
# this function adds a counter as the key of the enumerate object

x = ("apple", "banana", "cherry")
y = enumerate(x)
print(list(y))

print(".....eval()....")
# eval() evaluates the specified expression
x = 'print(57)'
print(x)

print(",,,,,,exec().....")
# The exec() function executes the specified Python code.
# The exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression
x = 'name = "John"\nprint(name)'
exec(x)

print(".....Filter().....")
# function returns an iterator were the items are filtered through a function to test if the item is accepted or not.

ages = [2, 5, 7, 28, 24, 19]


def myfunc(x):
    if x > 18:
        return True
    else:
        return False


adults = filter(myfunc, ages)

for x in adults:
    print(x)

print(".....float().....")
# converts the specified value into a floating point number
print(float(7))
x = float("3.500")
print(x)

print("......format().......")
# formats the specified value into a specified format
x = format(0.5, '%')
print(x)
x = format(255, 'x')
print(x)

print("....frozenset()......")
# The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).
list = ['a', 'b', 'c']
x = frozenset(list)
print(x)

# mylist = ['apple', 'banana', 'cherry']
# x = frozenset(mylist)
# x[1] = "strawberry"
# print(x) ---error ('frozenset' object does not support item assignment)

print("......getattr().....")


# returns the value of the specified attribute from the specified object
class Student:
    age = 19
    name = "abc"
    cls = 5


x = getattr(Student, 'cls')
print(x)


class Person:
    name = "John"
    age = 36
    country = "Norway"


x = getattr(Person, 'page', 'my message')
print(x)

print("......globals().....")
# The globals() function returns the global symbol table as a dictionary.
# A symbol table contains necessary information about the current program
x = globals()
print(x)

x = globals()
print(x["__file__"])

print("......hasattr()......")


# The hasattr() function returns True if the specified object has the specified attribute, otherwise False.
class Person:
    name = "John"
    age = 36
    country = "Norway"


x = hasattr(Person, 'age')
print(x)

print("...hash()....")
print("hash() ->Returns the hash value of a specified object")
print("help()	Executes the built-in help system")

print(".........hex()......")
x = hex(255)
print(x)
# The hex() function converts the specified number into a hexadecimal value.
# The returned string always starts with the prefix 0x.

print("..........id().......")
x = ('apple', 'banana', 'cherry')
y = id(x)
print(y)

# This value is the memory address of the object and will be different every time you run the program

print("......input().....")
# print('Enter your name:')
# x = input()
# print('Hello, ' + x)
print(",,,,..int()...")
x = int(3.5)
print(x)

print('......isinstance()......')
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.
x = isinstance("Hello", (str, float, int, str, list, dict, tuple))
print(x)


class myObj:
    name = "John"


y = myObj()

x = isinstance(y, myObj)

print(x)

print(".....issubclass()......")


# The issubclass() function returns True if the specified object is a subclass of the specified object, otherwise False.
class myAge:
    age = 36


class myObj(myAge):
    name = "John"
    age = myAge


x = issubclass(myObj, myAge)

print(x)
print(".....iter().....")
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))

print("///....len()....")
# The len() function returns the number of items in an object.
# When the object is a string, the len() function returns the number of characters in the string.
print(len("Hello"))
mylist = ["apple", "banana", "cherry"]
x = len(mylist)
print(x)

print(".....list().....")
# The list() function creates a list object.
# A list object is a collection which is ordered and changeable.
# x =('apple', 'banana', 'cherry')
# y=list(x)
# print(y)

print("....locals()....")
# The locals() function returns the local symbol table as a dictionary.
# A symbol table contains necessary information about the current program.
x = locals()
print(x)

print("......map()......")


# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
def myfunc(a):
    return len(a)


x = map(myfunc, ['apple', 'banana', 'cherry'])
for i in x:
    print(i)
print(x)


# convert the map into a list, for readability:print(list(x))


def myfunc(a, b):
    return a + b


x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(x)

# convert the map into a list, for readability:
#print(list(x))


print("....max...")
print(max(5,7))
x = max("Mike", "John", "Vicky")
print(x)
a = (1, 5, 3, 9)
x = max(a)
print(x)


print("....memoryview()....")
#The memoryview() function returns a memory view object from a specified object.
x = memoryview(b"Hello")

print(x)

#return the Unicode of the first character
print(x[0])

#return the Unicode of the second character
print(x[1])

print("....min()....")
# The min() function returns the item with the lowest value, or the item with the lowest value in an iterable.
# If the values are strings, an alphabetically comparison is done.
print(min(3,2))

print("/////next().....")
#The next() function returns the next item in an iterator.
x=iter(["a","b","c"])
print(next(x))
print(next(x))

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)

print("//////object()......")
#returns an empty object.You cannot add new properties or methods to this object.
#This object is the base for all classes, it holds the built-in properties and methods which are default for all classes.
x = object()
print(dir(x))

print(".....oct()....")
# The oct() function converts an integer into an octal string.
# Octal strings in Python are prefixed with 0o.
x=oct(2)
print(x)

print("....open()....")
#The open() function opens a file, and returns it as a file object.
# f=open("ab.txt","r")
# print(f.read())

print("......ord().....")
#The ord() function returns the number representing the unicode code of a specified character.
print(ord("s"))

print("......pow().....")
#Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
x=pow(4,3)
print(x)
#Return the value of 4 to the power of 3, modulus 5 (same as (4 * 4 * 4) % 5):

x = pow(4, 3, 5)
print(x)


print(".....print()....")
print("Hello", "how are you?", sep="---")
x = ("apple", "banana", "cherry")
print(x)

print("property -->  Gets, sets, deletes a property")

print("......range()......")
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
x=range(3,5)
for i in x:
    print(i)
#Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:

x=range(3,20,2)
for i in x:
    print(i)

print(".......repr().......")
print("repr()	-> Returns a readable version of an object")

print("........reversed().....")
#The reversed() function returns a reversed iterator object.
#it will reverse the sequence of a list and print each item
alph=["a","b","c","d"]
x=reversed(alph)
for i in x:
    print(i)

print(".......round().....")
#The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
x=round(5.7683)
print(x)
x=round(9.8376,2)
print(x)

print(".......The set()......")

#The items in a set list are unordered, so it will appear in random order.")
x=set(("apple","banana","cherry"))
print(x)

print(".......setattr().....")
#setattr() sets the value of a specified attribute of the specified object
class Book:
    BName:"Hp"
    Author:"JR"
    Age:57

setattr(Book,'Author','Rowling')
x=getattr(Book,'Author')
print(x)

print("......Slice().....")
#slice() returns a slice object

a=("a","b","c","d","e")
x=slice(2)
print(a[x])

#Create a tuple and a slice object. Use the step parameter to return every third item:

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])

a=("a","b","c","d","e")
x=slice(2,4)
print(a[x])

print(".....sorted().....")
#The sorted() function returns a sorted list of the specified iterable object.
#You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.
a = (1, 11, 2)

x = sorted(a)

print(x)

a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a)
print(x)

a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)

print("staticmethod()->Converts a method into a static method")

print("....str()....")
#The str() function converts the specified value into a string.
x=str(3.5)
print(x)
x = int("12")
print(x)

print("......sum().....")
a = (1, 2, 3, 4, 5)
x = sum(a, 7)
print(x)

a=(1,2,3,4,5)
print(sum(a))

print("//////super().....")
# The super() function is used to give access to methods and properties of a parent or sibling class.
# The super() function returns an object that represents the parent class.
class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()

print("////tuple....")
# The tuple() function creates a tuple object.
x = tuple(("apple", "banana", "cherry"))
print(x)


print("....type()....")
#The type() function returns the type of the specified object
a = ('apple', 'banana', 'cherry')
b = "Hello World"
c = 33

x = type(a)
y = type(b)
z = type(c)

print(x)
print(y)
print(z)


print("......vars.....")
# The vars() function returns the __dic__ attribute of an object.
# The __dict__ attribute is a dictionary containing the object's changeable attributes.
class Person:
  name = "John"
  age = 36
  country = "norway"

x = vars(Person)

print(x)
print(".......zip.....")
# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
#If one tuple contains more items, these items are ignored:

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

print(tuple(x))

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

print(tuple(x))

