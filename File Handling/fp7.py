#7.Python Program to Capitalize First Letter of Each Word in a File

f=open("myfile.txt","r")

for data in f:
    output=data.title()  #This will convert the content of that line with capitalized first letter of every word

print(output)