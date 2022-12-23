#9.Python Program to Extract Numbers from Text File


# Adding numbers to the existing file
f=open("myfile.txt","w")
data="7 add 8 remove 9 clear 1 store"
f.write(data)
f.close()

#Extracting numbers
f=open("myfile.txt","r")
count=0
content=f.readlines()
#print(content)
for line in content:
    for i in line:
        if i.isdigit():
            print(i)




