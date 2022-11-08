#13.Python Program to Sort a List According to the Second Element in Sublist

#Sorting by the use of sort() method
# While sorting via this method the actual content of the tuple is changed, and just like the previous method, in-place method of sort is performed.

def sortList(list1):
    list1.sort(key=lambda x:x[1]) #x[0]- names x[1]-values
    return list1

list11=[['rishav', 10], ['zen', 5], ['akash', 20], ['gaurav', 15]]
print(sortList(list11))

#Sorted() sorts a list and always returns a list with the elements in a sorted manner, without modifying the original sequence
def sortsublist(list2):
    return sorted(list2,key=lambda x:x[1])

print(sortsublist(list11))