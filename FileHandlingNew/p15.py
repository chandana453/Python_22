#15.A binary file school.dat has structure(rollno, name, class, fees)
# Write a definition for function total_fees( ) that reads each object of file and calculate the total fees of students and display the same.

import os.path

file_path='/Users/mounika/PycharmProjects/FileHandlingNew/school.dat'
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
    f=open("school.dat","ab")
    lst=[roll_no,Name,Class,fees]
    p.dump(lst,f)
    f.close()

def total_fees():
    f=open("school.dat","rb")
    total=0
    try:
        while True:
            lst=p.load(f)
            total+=lst[3]

    except EOFError:
        pass
    print("Total fees of students:", total)
    f.close()

def testProgram():
    createFile()
    total_fees()

testProgram()
