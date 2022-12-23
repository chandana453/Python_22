#14.Write a function to search and display details of student whose rollno is '1005' from the binary file student.dat having structure [rollno, name, class and fees]

import os.path

file_path='/Users/mounika/PycharmProjects/FileHandlingNew/student.dat'
file_size=os.path.getsize(file_path)
print("FILE SIZE:",file_size,"bytes")

import pickle as p
def createFile():
    while True:
        roll_no= int(input("Enter roll number:"))
        Name=input("Enter Student name:")
        Class=int(input("Enter class:"))
        fees = int(input("Enter fees:"))
        choice = input("wish to you enter another record?")
        if choice.upper() == 'N':
            break
    f=open("student.dat","ab")
    lst=[roll_no,Name,Class,fees]
    p.dump(lst,f)
    f.close()

def display():
    f=open("student.dat","rb")
    try:
        while True:
            lst=p.load(f)
            if lst[0]==1005:
                print(lst)

    except EOFError:
        pass
    f.close()

def testProgram():
    createFile()
    print("Displaying the information of the student with rollno:")
    display()

testProgram()


