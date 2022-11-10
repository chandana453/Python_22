#3.Python Program to Count the Number of Lines in Text File


#The readlines() are used to read all the lines at a single go and then return them as each line a string element in a list. This function can be used for small files

with open("First.txt","r") as file1:
    lines=len(file1.readlines())

print("Number of lines in file: ",lines)


#2nd approach

file10 = open("First.txt", "r")
count=0
content=file10.read()
lines=content.split("\n")

for i in lines:
    if i:
       count+=1

print("Number of lines in the file are: ",count)


