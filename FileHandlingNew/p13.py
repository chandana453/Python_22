# Given a binary file employee.dat, created using dictionary object having keys: (empcode, name, and salary)
#
# Write a python function that add one more record at the end of file.
# Write a python function that display all employee records whose salary is more that 30000


import os.path

file_path='/Users/mounika/PycharmProjects/FileHandlingNew/Employee.dat'
file_size=os.path.getsize(file_path)
print("FILE SIZE:",file_size,"bytes")

import pickle as p
def createFile():
    while True:
        d={}
        d["Empcode"]=int(input("Enter empcode:"))
        d["Name"] = input("Enter Name:")
        d["Salary"]=int(input("Enter Salary:"))
        choice = input("wish to you enter another record?")
        if choice.upper() == 'N':
            break
    f=open("Employee.dat","ab")
    p.dump(d,f)
    f.close()

def check_salary():
    f=open("Employee.dat","rb")
    try:
        while True:
            d = p.load(f)
            if d["Salary"]>30000:
                print(d)
    except EOFError:
        pass
    f.close()

def testProgram():
        createFile()
        print('Employee details having salary more than 30000')
        check_salary()


testProgram()
