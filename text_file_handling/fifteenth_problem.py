# A binary file players.dat, containing records of following list format: [code, name, country and total runs]
# Write a python function that display all records where player name starts from 'A'
# Write a python function that accept country as an argument and count and
# display the number of players of that country.
# Write a python function that add one record at the end of file.

import json


def add_record():
    data_add = {"code": int(input("enter the code")), "name": input("enter the name"),
                "country": input("enter the country name"), "runs": int(input("enter the runs scored"))}
    with open("players.dat", "ab") as file:
        pickle.dump(data_add, file)
    return "ok done"


# print(add_record())


def all_records():
    with open("players.dat", "rb") as file1:
        while True:
            try:
                # data = json.load(file1)
                data1 = file1.decode('utf-16').strip()
                data = json.load(data1)
                if data["name"][0] == "A":
                    print(data)
            except:
                raise

            return "ok done"


res = all_records()

print(res)


def country_guys(country):
    with open("players.dat", "rb") as file2:
        country_count = 0
        while True:
            try:
                data1 = pickle.load(file2)
                if data1["country"] == country:
                    country_count += 1
            except EOFError:
                pass
                break
    return country_count

# print(country_guys("india"))
