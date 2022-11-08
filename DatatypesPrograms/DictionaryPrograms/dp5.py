#5.Python Program to Remove a Key from a Dictionary
dict={"aa":10,"bb":20,"cc":30}

dict.pop("bb") #pop() and del are used to remove a key from dictionary
del dict["aa"]
print(dict)
# dict={"bb":30}
dict.update(dd=10,ee=30,ff=90)
print(dict)

# #2nd approach
def removeKey(dict):
    d={}
    for key,value in dict.items():  #adding the key,value pairs to the new dictionary
        if key!="dd":
            d[key]=value
    return d

print(removeKey(dict))


