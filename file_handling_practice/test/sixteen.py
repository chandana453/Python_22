# . Given a binary file game.dat, containing records of following list format: [game_name, participants]
#
# Write a function in Python that would read contents from the file game.dat and creates a file named basket.dat copying only those records from game.dat where the game name is "Basket Ball"

import pickle

path = "../text_file/game.dat"

with open(path,"ab") as file:
    game_name = input("enter the game name : ").upper()
    participants = int(input("enter the num of participants : "))
    data = {"game_name" : game_name, "participants" : participants}
    pickle.dump(data,file)




##function creates a new file if game entered is in game.dat file

def create_diff_game_file(game):
    with open(path,"rb") as file:
        try:
            while True:
                data = pickle.load(file)
                if data["game_name"] == game:
                    path_2 = f"../text_file/{game}.dat"
                    with open(path_2,"ab") as new_file:
                        pickle.dump(data,new_file)
        except Exception:
            print("end of file")

game_file_to_create = input("enter the game name : ").upper()
create_diff_game_file(game_file_to_create)