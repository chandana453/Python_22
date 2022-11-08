#11.Python Program to Remove Duplicates from a List
li1=[2, 4, 10, 20, 5, 2, 20, 4]
li1=list(set(li1))
print(li1)

#2nd approach
def remove_duplicates(list1):
    final_list=[]
    for i in list1:
        if i not in final_list:
            final_list.append(i)
    return final_list

print(remove_duplicates(li1))


#3.using dict.fromkeys()

list1=[2,3,3,4,2,2,1,5,7,9,10,7]
m=list(dict.fromkeys(list1))
print(m)