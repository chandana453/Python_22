'''
Please write a program using generator to print the even numbers
between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10
Hints:
Use yield to produce the next value in generator.
In case of input data being supplied to the question, it should be
assumed to be a console input.
'''


l=[1,2,3,4,5,6,7,8,9,10]
for i in range(10):
    if i % 2 == 0:
        print(i)