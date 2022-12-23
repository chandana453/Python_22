f=open("SampleFile.txt","w") #creates a file if it doesn't exist

for i in range(10):
    f.write("Hello,this is line %d\r\n" % (i+1))

#f.write("Hello, Python programmer")
f.close()
# f=open("SampleFile.txt","r")
# print(f.read())

#1.Python Program to Read the Contents of the File
f1=open("SampleFile.txt","r")
print(f1.read())



