#1.Write a program to find the characters which matches with the keys of given dictionary and replace them with the associated value.
# d = {'a' : 'b', 'b' : 'c', 'c': 'a' }
# Input: abc
# Output: bca

dict={"a":"b","b":"c","c":"a"}
st=input("enter string containing only abc: ")
new_Str=""
for ch in st:
    if ch in dict:
        new_Str += str(dict[ch])

print(new_Str)