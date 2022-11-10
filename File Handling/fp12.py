#12.Python Program to Read a String from the User and Append it into a File

f=open("SampleFile.txt","a")
str=input("Enter a string to append: ")
f.write("\n")
f.write(str)
f.close()

data=open("SampleFile.txt","r")
print(data.read())
