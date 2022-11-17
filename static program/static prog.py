"""python program to create a class which perform Basic calculator operations."""
# class cal:
#     def __int__(self,a,b):
#        self.a=a
#        self.b=b
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mul(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b
# A=int(input("enter the first number"))
# B=int(input("enter the second number"))
# obj1=cal()
# print("obj1.add(A,B),Obj1.sub(A,B),obj1.mul(A,B),obj.1div(A,B)")
"""print program to append,delete and display elements of a list using classes."""
# a=[3,4,39,9]
# class method:
#     def __int__ (self,x):
#         self.x=x
#     def add(self,x):
#         a.append(x)
#         return a
#     def remove(self,x):
#         a.remove(x)
#         return a
#     def dis(self):
#         return a
# obj1=method()
# print(obj1.add(10))
"""Python Program to Find the Area of a Rectangle using Classes."""
# class rec:
#     def area(selfself,length,breadth):
#         return length*breadth
# A=int(input("enter the length of rectangle"))
# B=int(input("enter the length of rectangle"))
# obj1=rec()
# print("the area of reactangle",obj1.area(A,B))
# """python program to implement static method and class method and instance method."""
# class person:
#   def __init__(self,name,age,can_vote):
#     self.name=name
#     self.age=age
#     self.can_vote=can_vote
#   @staticmethod
#   def isEligible(age):
#     if age>18:
#         return True
#     else:
#         return False
#   @classmethod
#   def create(cls,name,age):
#     if cls.isEligible(age)==True:
#         return cls(name,age,"Yes")
#     else:
#         return cls(name,age,"no")
# st1=person.create("John",25)
# st2=person.create("Adam",17)
# print("can",st1.name,"vote)",st1.can_vote)
# print("can",st2.name,"vote",st2.can_vote)
"""Write a program to find the characters which matches with the keys of given dictionary and replace them with the associated value.
d = {'a' : 'b', 'b' : 'c', 'c': 'a' }
input:abc
Output: bca"""
# d={'a':'b','b':'c','c':'a'}
# input=input()
# for ele in input:
#     if ele in d.keys():
#        print(d[ele],end=(""))
"""Write a program to print the factorial of a given number using a while loop. Don't use any predefined or user-defined functions."""
# my_input=int(input("Enter the value-"))
# i=1
# fact=1
# while i<=my_input:
#    fact=i*fact
#    i=i+1
# print(fact)
"""Write a Python program to get the maximum and minimum value from a list without using any predefined function."""
# a=[int(i) for in input().split(",")]
# b=sorted(a)
# print("The min value",b[0])
# print("The max value",b[-1])
"""Define a list that contains the marks percentage for the students. Print a list that contains the Grades of the students.
  The grading will be decided by the following conditions.
  A+ if the percentage is greater than 90
  A if the percentage is less than or equal to 90 and greater than 70
  B if the percentage is less than or equal to 70 and greater than 50
  C if the percentage is less than or equal to 50 and greater than 35
  F if the percentage is less than or equal to 35."""
# inut=[int(i)for i in input(9).split(",")]
# output=[]
# for i in input:
#     if i>90:
#        output.append("A+")
#     elif i<=90 and i>70:
#          output.append("A")
#     elif i<=70 and i>50:
#         output.append("B")
#     else:
#       output.append("F")
# print(output)
"""Print the type of integer until the given index position in characters(Even or Odd) exclude index 0.
 Input: [0,1,2,3,4,6,7,8]
 index: 5
 Output: ['Odd','Even', 'Odd', 'Even', 'Even']."""
# input=[0,1,2,3,4,5,6,7,8]
# output=[]
# index=5
# for i in input[0:7]:
#   if i == input[0]:
#       pass
#   elif i == input[5]:
#       pass
#   else:
#     if i%2==0:
#        output.append("Even")
#     else:
#        output.append("odd")
"""Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
For example, if the limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20."""
# total_sum=0
# for i in range(1000):
#     if (i%3 == 0 or i%5 == 0):
#         total_sum = total_sum+i
#         print(total_sum)
"""Write a program to print the following:
*
**
***
****
*****."""
# def pypart(n):
#      for i in range(0, n):
#          for j in range(0, i+i):
#              print("*",end="")
#          print("\r")
# n=5
# pypart(n)
"""Write a function called fizz_buzz that takes a number.
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number."""
# def fizzler(num):
#     if num % 3 !=0 and num % 5!=0:
#         return num
#     if num % 3 ==0 and num % 5 == 0:
#         return "FizzBuzz"
#     if num % 3 == 0:
#         return "Fizz"
#     return "Buzz"
# if __name__=="main__":
#     number = int(input("Enter a number"))
#     print(fizzler(number))
"""Write a program to reverse a string word by word along with reverse the characters in each word."""
# def reverse_word(s, start ,end):
#  while start < end:
#    s[start],s[end] = s[end],s[start]
#    start = start + 1
#    end -=1
#    s ="i like this program very much"
#    s = list(s)
#    start = 0
#    while True:
#     try:
#         end = s.index(' ',start)
#         reverse_word(s,start,end -1)
#         start = end + 1
#     except Exception as e:
#         reverse_word(s, start,len(s) - 1)
#         break
#    s.reverse()
#    s = "".join(s)
#    print(s)
"""Define a list and create a dictionary where the dictionary key is an index of the element and value is an element in the list."""
# l=[0,2,4,16,28]
# d={}
# for i in range(len(l)):
#     d[i]=l[i]
# for key,value in d.items():
#     print(key,":",value)

