#11.Python Program to Count Number of Lowercase Characters in a String

str="ProgrammIng"
count=0
for i in str:
    if i.islower():
        count+=1

print(count)
