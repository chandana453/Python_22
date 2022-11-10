#4.Python Program to Count the Number of Blank Spaces in a Text File
f1=open("myfile.txt","r")
count=0

while True:
        #reading the contents and storing in a variable
        char=f1.read(1)
        if char.isspace():
            count+=1
        if not char:
            break

print("Number of blank spaces in file are: ",count)



