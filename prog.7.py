# Question 7
# Level 2
# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-
# dimensional array. The element value in the i-th row and j-th column
# of the array should be i*j.
# Note: i=0,1..,x-1;j=0,1,;y-1
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
# Hints:
# Note: In case of input data being supplied to the question, it should
# be assumed to be a console input in a comma-separated form.
# Solution:

input_str=input(100)
dimensions[(int(x)for x in input_str.split(','))]
rownum=dimensions[0]
colnum=dimensions[1]
multilist=[[0 for col in range(colnum)]for row in range(rownum)]
for col in range(colnum):
    multilist[row][cool]=row*col
print (multilist)