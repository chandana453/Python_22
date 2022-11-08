'''
Define a custom exception class which takes a string message as
attribute.
Hints:
To define a custom exception, we need to define a class inherited from
Exception.
'''

"""
My own exception class
Attributes:
    msg== explaination of the error
"""
class myerror():
  def __init__(self,msg):
    self.msg=msg
  def error(self):
      print(self.msg)

error= myerror("Something's wrong")
print(error)
