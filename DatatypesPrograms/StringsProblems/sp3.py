#3.Python Program to Remove the nth Index Character from a Non-Empty String
str="Programming language"
index_to_remove=10

def removeIndex(str):
    modified_string=""
    for i in range(len(str)):
        if i!=index_to_remove:
            modified_string+=str[i]
    return modified_string

print(removeIndex(str))


#2nd approach
string1="python programming"
odd_index=4
first_part = string1[0:odd_index]
second_part = string1[odd_index + 1:]

result=first_part+second_part
print(result)


