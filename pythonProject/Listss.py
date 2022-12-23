#List is a collection which is ordered and changeable. Allows duplicate members.
Mylist=["c","c++","java","python"]
print(Mylist)
print(type(Mylist))

#len of a list
print(len(Mylist))

#list constructor to create a new list
myList=list(("Python","Java","C"))
print(myList)

#Access items
print(Mylist[2])

print(Mylist[1:3])
print(Mylist[:3])
print(Mylist[:])
print(Mylist[-1])
print(Mylist[-3:])

if "java" in Mylist:
    print("yes")

print("----edited----")
print(len(Mylist))
Mylist[3]="js"
print(Mylist)

Mylist[1:3]=["python","django"]
print(Mylist)

Mylist[1:3]=["java","aws","c++"]
print(Mylist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insertion
print("\n")
print("**INSERTION**")
print(myList)
myList.insert(3,"python")
myList.insert(1,"Django")
print(myList)

#To add an item to the end of the list, use the append() method:
myList.append("c++")
print(myList)


#To append elements from another list to the current list, use the extend() method.
print(myList)
print(Mylist)
myList.extend(Mylist)
print(myList)


#extend() is used to append any type of iterables like sets,tuples and dictonaries along with lists
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#The remove() method removes the specified item.
myList.remove("c++")
print(myList)
myList.pop() #removes last element
print(myList)
myList.pop(5)
print(myList)

#The del keyword also removes the specified index:
print("DELETION")
del myList[2]
print(myList)

del thislist

myList.clear()
print(myList)

print("Loop Through a List")
print(Mylist)
for x in Mylist:
    print (x)
for k in range(len(Mylist)):
    print (Mylist[k])

#while loop

newlist=["abc","def","ghi"]
i=0
while(i < len(newlist)):
    print(newlist[i])
    i=i+1
#shortest syntax of for loop
print(Mylist)
[print(k) for k in Mylist]


print("List Comprehension")
#newest=[]
#for i in Mylist:
#    if "a" in i:
#        newest.append(i)
#
#print (newest)


newest=[x for x in Mylist if "a" in x]
print(newest)

newlist1 = [x for x in range(10)]

print(newlist1)

newlist2=[x for x in range(10) if x<5]
print(newlist2)

#Set the values in the new list to upper case:

newlist = [x.upper() for x in Mylist]
print(newlist)

newlist=["hi" for x in Mylist]
print(newlist)

#Return "orange" instead of "banana":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
#The expression in the example above says:

#"Return the item if it is not banana, if it is banana return orange".

#Reverse list
list5=[1,4,3,2,5]
list5.sort()
print(list5)
list5.sort(reverse = True)
print(list5)

#You can also customize your own function by using the keyword argument key = function.
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist.sort(key=str.lower)
print(thislist)

thislist.reverse()
print(thislist)

exlist=Mylist.copy()
print(exlist)

klist=list(Mylist)
print(klist)

print("JOIN LISTS")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3=list1+list2
print(list3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3,4,5,6,7]
list1.extend(list2)
print(list1)
for x in list2:
    list1.append(x)
print(list1)


print("COUNT")
fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)
print(x)

print("INDEX")
fruits = [4, 55, 64, 32, 16, 32]

x = fruits.index(32)
print(x)