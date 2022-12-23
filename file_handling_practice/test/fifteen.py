# A binary file players.dat, containing records of following list format: [code, name, country and total runs]
#
# Write a python function that display all records where player name starts from 'A'
# Write a python function that accept country as an argument and count and display the number of players of that country.
# Write a python function that add one record at the end of file.

import pickle

path = "../text_file/players.dat"


## adds player to the players file


with open(path,"ab") as player_file:
    code = int(input("enter the player code : "))
    name = input("enter the player name : ").upper()
    country = input("country name : ").upper()
    total_runs = int(input("enter the player total runs : "))

    data = {"code": code, "name": name, "country": country, "total_runs": total_runs}
    pickle.dump(data,player_file)


## a function that displays all records of player whose name starts with "A"


def check_name(alp):
    try:
        with open(path,"rb") as file:
            while True:
                data = pickle.load(file)
                if data["name"][0] == alp :
                    print(data)
                else:
                    print("player doesnot exist")
    except Exception:
        print("end of the file")


alpha = input("enter the alphabet to check: ").upper()
check_name(alpha)



## function that accept country as an argument and count and display the number of players of that country.

def same_country(country):
    try:
        with open(path,"rb") as file:
            count = 0
            while True:
                data = pickle.load(file)
                if data["country"] == country:
                    count += 1

    except Exception:
        print("end of file")
    finally:
        print(f"the total no. of players from {country} is {count}")

country = input("enter the country name to check: ")

same_country(country)