#problem5
'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''
import unittest
n = input("the string input ")
get_string = n.split()
upper_string = n.upper()
print(get_string)
print(upper_string)
#problem6
'''
Write a program that calculates and prints the value according to the
given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a
comma-separated sequence.
'''
import math
l=[]
C = (50)
H = (30)
input_value = (input("< "))
items = input_value.split(',')
print(items)
for d in items :
    l.append(str(int(round(math.sqrt(2 * C * float(d)) / H))))
print(','.join(l))
#problem7
'''
Write a program which takes 2 digits, X,Y as input and generates a 2-
dimensional array. The element value in the i-th row and j-th column
of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1.
'''
input_str = input("< ")
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for col in range(colNum):
    multilist[row][col]= row * col
print (multilist)

#problem 8
'''
Write a program that accepts a comma separated sequence of words as
input and prints the words in a comma-separated sequence after sorting
them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''
word = input("the input value ")
value = word.split(',')
value.sort()
print(value)
'''
#problem 9
Write a program that accepts sequence of lines as input and prints the
lines after making all characters in the sentence capitalized.
'''
message =input("the message ")
value = message.upper()
print(value)
#problem 10
'''
Write a program that accepts a sequence of whitespace separated words
as input and prints the words after removing all duplicate words and
sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
'''
message = input("message ")
set_value = message.split(" ")

print(','.join(sorted(list(set(set_value)))))
'''
# problem 11
Write a program which accepts a sequence of comma separated 4 digit
binary numbers as its input and then check whether they are divisible
by 5 or not. The numbers that are divisible by 5 are to be printed in
a comma separated sequence.
Example:
0100,0011,1010,1001
'''
value = []
n = input("the binary ")
split_bin = n.split(',')
for i in split_bin:
    inti = int(i,2)
    if not inti % 5 :
        value.append(i)
print(','.join(value))
# problem 12
'''
Write a program, which will find all such numbers between 1000 and
3000 (both included) such that each digit of the number is an even
number.
The numbers obtained should be printed in a comma-separated sequence
on a single line.
'''
m =[]
for i in range(1000, 3000+1):
    if int(i / 2 ==0) :
        m.append(i)
print(m)
# problem 13
'''
Write a program that accepts a sentence and calculate the number of
letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
'''
message = input("< ")
d={"NUMBERS":0, "CHARACTERS":0}
for  h in message:
 if h.isdigit():
     d["NUMBERS"]+=1
 elif h.isalpha():
     d["CHARACTERS"]+=1
 else:
     pass
print(d["NUMBERS"])
print(d["CHARACTERS"])
'''
# problem 14
Write a program that accepts a sentence and calculate the number of
upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
'''
value = (input("< "))
d = {"UPPER" :0, "LOWER" :0 }
for i in value :
    if i.isupper():
        d["UPPER"]+=1
    elif i.islower():
        d["LOWER"]+=1
    else :
        pass
print(d["UPPER"])
print(d["LOWER"])

# problem 15
Write a program that computes the value of a+aa+aaa+aaaa with a given
digit as the value of a.
value = int(input("< "))
n1 = ("%s"(%a))
n2 = ("%s%s"%(a,a))
n3 = ("%s%s%s"%(a,a,a))
n4 = ("%s%s%s%s"%(a,a,a,a))
n = n1 +n2 +n3 +n4
print(n)

# problem 16
Use a list comprehension to square each odd number in a list. The list
is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
values = input("< ")
numbers = [i for i in values.split(",") if int(i)%2!=0] #list comprehension
print (",".join(numbers))

#problem17
Write a program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is
shown as following:
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

netAmount = 0
while True:
 i = input("the required input ")
 if not i:
     break
 values = i.split(" ")
 operation = values[0]
 amount = (values[1])
 if operation=="D":
     netAmount+=amount
 elif operation=="W":
     netAmount-=amount
 else:
     pass
print(netAmount)
#problem18
A website requires the users to input username and password to
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

import re
value = []
items=[i for i in input("< ").split(',')]
for s in items:
 if len(s)<6 or len(s)>12:
     continue
 else:
     pass
 if not re.search("[a-z]",s):
     continue
 elif not re.search("[0-9]",s):
     continue
 elif not re.search("[A-Z]",s):
     continue
 elif not re.search("[$#@]",s):
     continue
 elif re.search("\s",s):
     continue
 else:
     pass
 value.append(s)
print (",".join(value))

#problem19
You are required to write a program to sort the (name, age, height)
tuples by ascending order where name is string, age and height are
numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.

from operator import itemgetter, attrgetter

l = []
while True:
    s = input("< ")
    if not s:
        break
    l.append(tuple(s.split(",")))
    print (sorted(l, key= itemgetter(0,1,2)))
#problem20


