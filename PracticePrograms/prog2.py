#2.Write a program to print the factorial of a given number using a while loop. Don't use any predefined or user-defined functions.

n=int(input("Enter number"))
fact=1
while n>0:
    fact=n*fact
    n=n-1
print(fact)