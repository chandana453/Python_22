#17.Given a binary file game.dat, containing records of following list format: [game_name, participants]

# Write a function in Python that would read contents from the file game.dat and creates a file named basket.dat copying only those records from game.dat
# where the game name is "Basket Ball"


import os.path

file_path='/Users/mounika/PycharmProjects/FileHandlingNew/game.dat'
file_size=os.path.getsize(file_path)
print("FILE SIZE:",file_size,"bytes")

import pickle as p
def create():
    record = []
    while True:
        game_name = input("enter a game:")
        participant = input("enter name:")
        data = [game_name, participant]
        record.append(data)
        choice = input(" wish to you enter another record?")
        if choice.upper() == 'N':
            break
    f = open('game.dat', 'ab')
    p.dump(record, f)  # dump() writes the object into the opened file
    f.close()

def copy():
    f1=open("game.dat","rb")
    f2=open("basketball.dat","wb")
    try:
        while True:
            data=p.load(f1)
            if data[0]=="BasketBall":
                p.dump(data,f2)
    except EOFError:
        pass
    f1.close()
    f2.close()


def testProgram():
    create()
    print("Copied BasketBall data into new file")
    copy()


testProgram()
