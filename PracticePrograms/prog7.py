#7.)Write a program to print the following:
# *
# **
# ***
# ****
# *****

def Pyramid(n):
    #outer loop to handle number of rows
    for i in range(0,n):
        #inner loop to handle number of columns
        for j in range(0,i+1):
            print("*",end="")
        # ending line after each row
        print("\r")

n=int(input("Enter number"))
Pyramid(n)