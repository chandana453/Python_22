"""Define a custom exception class which takes a string message as
attribute.
Hints:
To define a custom exception, we need to define a class inherited from
Exception."""
class MyError:
   def __init__(self, msg):
     self.msg = msg
   def error(self):
      print(self.msg)
error = MyError("something wrong")
print(MyError)