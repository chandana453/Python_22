#2.Python Program to Copy One File to Another File

#When you use with statement with open function, you do not need to close the file at the end, because with would automatically close it for you.

#creating a empty file and adding content to it
f=open("First.txt","a")
f.write("Python Programming : Content of first file")
f.close()

#copying the contents
with open("First.txt","r") as firstfile,open("Second.txt","w") as secondfile:
   for i in firstfile:
       #write the contents of First.txt into Second.txt
       secondfile.write(i)


f1=open("Second.txt","r")
print(f1.read())




