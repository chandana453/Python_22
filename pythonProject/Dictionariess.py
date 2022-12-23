mydict={
    "name":"abc",
    "age":25,
     "gender":"female"
}
print(mydict)
print(mydict['gender'])

x=mydict.get("name")
print(x)

x=mydict.keys()
print(x)

mydict["school"]="defgh"
print(mydict)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
print(car.values())

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
#Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
print(car.items())
car["year"]=2022
print(car)

if "model" in car:
  print("Yes, 'model' is one of the keys")

  #The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.
#
# Example
# Update the "year" of the car by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

thisdict.update({"example":"sample"})
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("brand")
thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# You can loop through a dictionary by using a for loop.
#
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
#
# Example
# Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)

#to print all values in a dictionary
for x in thisdict:
    print(thisdict[x])
# You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)
# Example
# You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)

  #Loop through both keys and values, by using the items() method:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for (x,y) in thisdict.items():
    print(x,y)
#The fromkeys() method returns a dictionary with the specified keys and the specified value.
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

car["year"] = 2018

print(x)

# Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)