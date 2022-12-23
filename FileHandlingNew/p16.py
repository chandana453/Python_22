#16.A binary file players.dat, containing records of following list format: [code, name, country and total runs]

# Write a python function that display all records where player name starts from 'A'
# Write a python function that accept country as an argument and count and display the number of players of that country.
# Write a python function that add one record at the end of file.

import os.path

file_path='/Users/mounika/PycharmProjects/FileHandlingNew/Players.dat'
file_size=os.path.getsize(file_path)
print("FILE SIZE:",file_size,"bytes")

import pickle as p
def create_file():
    while True:
        code=int(input("ENter code:"))
        name=input("Enter name:")
        country=input("ENter country:")
        total_runs=int(input("Enter total_runs:"))
        choice = input("wish to you enter another record?")
        if choice.upper() == 'N':
            break
    f=open("Players.dat","ab")
    lst=[code,name,country,total_runs]
    p.dump(lst,f)
    f.close()

def display_name():
    f=open("Players.dat","rb")
    try:
        while True:
            lst=p.load(f)
            if lst[1][0]=='A':
                print(lst)
    except EOFError:
        pass
    f.close()

def display_country(country):
    f=open("Players.dat","rb")
    count=0
    try:
        while True:
            lst=p.load(f)
            if lst[2]==country:
                count+=1
    except EOFError:
        pass
    print(count)
    f.close()


def testProgram(country):
    create_file()
    print("Displaying names starting with A")
    display_name()
    print(f"Number of players from {country}")
    display_country(country)

testProgram("India")




