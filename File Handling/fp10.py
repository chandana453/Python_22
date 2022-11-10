#10.Python Program to Print the Contents of File in Reverse Order
# f=open("myfile.txt","r")
# print(f.read())


# reversed() function produces a reverse iterator and rstrip() strips all the blank spaces from the end of the line
for line in reversed(list(open("myfile.txt"))):
    print(line.rstrip())

