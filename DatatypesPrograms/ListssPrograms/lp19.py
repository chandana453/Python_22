#19.Python Program to Find the Union of Two Lists
def unionlists(list1,list2):
    new_list=list1+list2
    print(new_list)
    print(list(set(new_list))) #to remove duplicates

lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
unionlists(lst1,lst2)

#2nd approach
def unionOfLists(list1,list2):
    #final_list = list(set(list1) | set(list2)) # |  - union operator
    final_list=list(set().union(list1,list2))
    return final_list
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(unionOfLists(lst1, lst2))

