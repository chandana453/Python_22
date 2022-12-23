#STRING FORMATTING

# name='Bob'
# greeting="Hello, {}"
# with_name=greeting.format(name)
# with_name=greeting.format("ROLF")  #this executes
# print(with_name)



#2 Reading user input

# name= input("ENter your name:")
# print(name)
#
# square_feet=input("Enter Square feet:")
# square_metres=int(square_feet)/10.8
# print(f"{square_feet} square feet is {square_metres} square metres")

x = 4863.4343091
print(f'{x:.3f}')
print(f'{x:.2f}')

print(f"{x:.6}")          # f-string version
print("{:.6}".format(x))  # format method version

# name='Mounika'
# greeting=f'hello, {name}'
# print(greeting)
# print("hello, {}".format(name))
#
# name=input("Enter name:")

# Then, print "Hello, NAME", where NAME is the user's name
#print(f"Hello, {name}")
#print("Hello, {}".format(name))

# age=int(input("Enter your age:"))
# months=age*12
# seconds=months*60*60
# print(f"{age} years, {months} months and {seconds} seconds old")



#ADVANCED SET OPERATIONS

art={"Bob","Jen","Roy","Anne"}
science={"Jen","Anne","Rob","Rolf"}

#To get Difference (students part of only science) --- DIFFERENCE
diff=science.difference(art)
print(diff)

#To get Difference (students part of only art) --- DIFFERENCE
diff1=art.difference(science)
print(diff1)

#Total no of students  ---- UNION
Total=art.union(science)
print(Total)

#STudents who study both art and science: --- INTERSECTION (common in both the sets)
Both=art.intersection(science)
print(Both)


#update() to add String and Dictionary to Set
# string
alphabet = 'odd'

# sets
number1 = {1, 3}
number2 = {2, 4}

# add elements of the string to the set
number1.update(alphabet) #The method breaks down the string into individual characters and adds them to the set number1.

print('Set and strings:', number1)

# dictionary
key_value = {'key': 1, 'lock' : 2}

# add keys of dictionary to the set
number2.update(key_value)

print('Set and dictionary keys:', number2)
#If dictionaries are passed to the update() method, the keys of the dictionaries are added to the set.


#List COMPREHENSION

l=[1,3,5]
doubled=[x*2 for x in l]
print(doubled)

# friends=["sam","sammy","Rob","saurabh","jen"]
# friends_s=[friend for friend in friends if friend.startswith("s")]
# print(friends_s)

#DICTIONARIES

friends=[
    {"name":"A","age":20},
    {"name":"B","age":25},
    {"name":"C","age":24}
]

print(friends)
print(friends[1]["name"])

students_attendance={"Adam":98,"Bob":80,"Anne":92}

for students,attendance in students_attendance.items():
    print(f"{students} : {attendance}")

for students in students_attendance:
    print(students)   #prints keys

for students in students_attendance.values():
    print(students)


