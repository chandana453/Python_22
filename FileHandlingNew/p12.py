#12.A binary file "STUDENT.DAT" has structure (admission_number, Name, Percentage). Write a function count_rec() in Python that would read contents of the file "STUDENT.DAT" and display the details of those students whose percentage is above 75. Also display number of students scoring above 75%

import os.path

file_path='/Users/mounika/PycharmProjects/FileHandlingNew/Student.dat'
file_size=os.path.getsize(file_path)
print("FILE SIZE:",file_size,"bytes")

import pickle as p
def createFile():
    while True:
        Admission_number= int(input("Enter admission number:"))
        Name=input("Enter Student name:")
        Percentage=int(input("Enter Percentage:"))
        choice = input("wish to you enter another record?")
        if choice.upper() == 'N':
            break
    f=open("Student.dat","ab")
    lst=[Admission_number,Name,Percentage]
    p.dump(lst,f)
    f.close()

def count_rec():
        f=open("Student.dat","rb")
        count = 0
        try:
            while True:
                lst=p.load(f)
                if lst[2] > 75:
                    print(lst[0], lst[1], lst[2])
                    count+=1

        except EOFError:
            pass
        f.close()

        print("count",count)


def testProgram():
    createFile()
    print('Info of students whose percentage is above 75')
    count_rec()


testProgram()

