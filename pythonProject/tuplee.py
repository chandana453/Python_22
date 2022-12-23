thistuple=("java","c","python")
print(thistuple)

print(len(thistuple))
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

print("Tuple Items - Data Types")
thistup1=("JAVA","C","DJANGO")
thistup2=(3,4,5,6,7)
thistup3=(True,False,True)

print(thistup1)
print(thistup2)
print(thistup3)

thistup4=("python",True,27,"C")
print(thistup4)

#Using the tuple() method to make a tuple: TUPLE CONSTRUCTOR
thistup=tuple(("yes","no","maybe"))
print(thistup)


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[1])
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Negative indexing means starting from the end of the tuple.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,

if "banana" in thistuple:
    print("yes")

#Convert the tuple into a list to be able to change it:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
tupletolist = list(thistuple)
tupletolist[1]="beetroot"
print(tupletolist)
thistuple=tuple(tupletolist)
print(thistuple)

#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#ADDING ELEMENTS(Convert the tuple into a list to be able to change it)


#1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
thistup=("a","b","c","d")
thislist=list(thistup)
thislist.append("e")
thistup=tuple(thislist)
print(thistup)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
thistu1=("dd","aa")
thistu2=("bb",)
thistu1+=thistu2
print(thistu1)


#REMOVING Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
x=list(thistuple)
x.remove("cherry")
thistuple=tuple(x)
print(thistuple)

#The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists



#Unpacking a Tuple
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

#Example
#Packing a tuple:

fruits = ("apple", "banana", "cherry")

#In Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")
(red,yellow,green)=fruits
print(red)
print(yellow)
#print(green)

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

#Example
#Assign the rest of the values as a list called "red":
print("------------ASTERISK__________(*)")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
