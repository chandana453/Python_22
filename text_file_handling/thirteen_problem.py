# Given a binary file employee.dat, created using dictionary object having keys: (empcode, name, and salary)
# Write a python function that add one more record at the end of file.
# Write a python function that display all employee records whose salary is more that 30000

import pickle


def add_record():
    data_rcd = {"empcode": 1003, "name": "sukumar", "salary": 34000}
    with open("employee.dat", "ab") as file:
        pickle.dump(data_rcd, file)
    return "ok done"


# print(add_record())

def display_record():
    with open("employee.dat", "rb") as file1:
        while True:
            try:
                data = pickle.load(file1)
                # print(data)
                if data["salary"] > 30000:
                    print("the details of employee whose salary above 30000", data)
            except EOFError:
                pass
                break
    return "done"

print(display_record())









