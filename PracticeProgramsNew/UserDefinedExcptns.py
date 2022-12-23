#4.Write a python program to demonstrate user-defined exceptions.
#1st example

class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass

class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass

#number you need to enter
n=7
while True:
    try:
        num = int(input("Enter a number: "))
        if num < n:
            raise ValueTooSmallError
        elif num > n:
            raise ValueTooLargeError
        break

    except ValueTooLargeError as err:
        print("Value you entered is larger, Try again!",err)

    except ValueTooSmallError as err:
        print("Value you entered is smaller, Try again",err)

print("Congratulations! You guessed it correctly.")



#2nd example
class MyError(Exception):

   def __init__(self,value):
       self.value=value

  # __str__ is to print() the value
   def __str__(self):
      return(repr(self.value))

try:
    raise (MyError("Error Occured"))  #raise keyword is used to raise an exception and can define what kind of error to raise, and the text to print to the user.
    #The raise keyword raises an error and stops the control flow of the program.

   # Value of Exception is stored in error
except MyError as error:
    print('A New Exception occurred: ', error.value)



