#11.A binary file "Book.dat" has structure [BookNo, Book_Name, Author, Price].
# i. Write a user defined function createFile() to input data for a record and add to Book.dat.
# ii. Write a function countRec(Author) in Python which accepts the Author name as parameter and count and return number of books by the given Author are stored in the binary file "Book.dat"

import os.path

file_path='/Users/mounika/PycharmProjects/FileHandlingNew/Book.dat'
file_size=os.path.getsize(file_path)
print("FILE SIZE:",file_size,"bytes")

import pickle as p
def createFile():
    while True:
        BookNo=int(input("Enter Book Number:"))
        BookName = input("Enter Book Name:")
        Author=input("Enter Author:")
        Price=float(input("Enter Price:"))
        choice = input("wish to you enter another record?")
        if choice.upper() == 'N':
            break
    lst=[BookNo,BookName,Author,Price]
    f=open("Book.dat","ab")
    p.dump(lst,f)
    f.close()

def countRec(Author):
     count=0
     with open("Book.dat","rb") as f:
        try:
            while True:
                lst=p.load(f)
                if Author==lst[2]:
                    count+=1
        except EOFError:
                pass

     return count




def testProgram():
    createFile()
    print('Number of books by the given Author')
    n=countRec("hoover")
    print(n)


testProgram()
