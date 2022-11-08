#20.Python Program to Find the Intersection of Two Lists
def intersectionOfLists(list1,list2):
    #new_list=set(list1) & set(list2)
    new_list=[x for x in list1 if x in list2]
    return new_list


l1 = [40, 90, 11, 58, 31, 66, 28, 54, 79]
l2 = [58, 90, 54, 31, 45, 11, 66, 28, 26]
print(intersectionOfLists(l1,l2))