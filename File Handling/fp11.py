#11.Python Program to Append the Content of One File to the End of Another File

input=open("SampleFile.txt","r")
data=input.read()
input.close()

output=open("myfile.txt","a")
output.write(data) #appending the content of samplefile to myfile
output.close()


# data=open("SampleFile.txt","r")
# print(data.read())

data1=open("myfile.txt","r")
print(data1.read())

