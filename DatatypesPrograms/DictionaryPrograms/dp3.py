#3.Python Program to Find the Sum of All the Items in a Dictionary
def sum_items(dict):
    return sum(dict.values())
dict={"a":10,"b":20,"c":30}
print(sum_items(dict))

def sumItems(dict):
    sum=0
    for i in dict.values():
        sum=sum+i
    return sum
dict={"a":100,"b":200,"c":30}
print(sumItems(dict))



# def sumOfItems(dict):
#     list1=[]
#     for i in dict:
#         list1.append(dict[i])
#     result= sum(list1)
#     return result

# dict={"a":10,"b":20,"c":30}
# print(sumOfItems(dict))

