#2.Python Program to Add a Key-Value Pair to the Dictionary

dict={"name":"john","age":20,"gender":"male"}

dict1={"address":"hyd"}
dict.update(dict1)
dict.update(key1="garbage")
dict["key2"]="sample"
print(dict)