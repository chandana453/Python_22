#decorators are used to modify the behaviour of function or class. In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

def lowercase(text):
    return text.lower()

def uppercase(text):
    return text.upper()

def message(func):
    # storing the function in a variable
    msg=func("hi,i'm new to python programming")
    print(msg)

message(lowercase)
message(uppercase)


#2nd example

# defining a decorator
def python_decorator(func):
   def wrapper():
      print("Text before calling the function")
      func()
      print("Text after calling the function")
   return wrapper

@python_decorator
def tutorials_decorator():
   print("Hello!!!")

tutorials_decorator()

#3rd example

def div(a,b):
     print(a/b)

def smart_fun(func):

    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div=smart_fun(div)
div(5,10)