# A binary file "student.dat" has structure (admission_number, Name, Percentage).
# Write a function count_rec() in Python that would read contents of the file "student.dat" and display the details of
# those students whose percentage is above 75. Also display number of students scoring above 75%

import pickle

data = {"admission_number": 103, "Name": "Madhav", "Percentage": 72}

fo = open("student.dat", "ab")

# pickle.dump(data, fo)

fo.close()


def count_rec():
    with open("student.dat", "rb") as ch:
        count = 0
        while True:
            try:
                data_get = pickle.load(ch)
                # print(data_get)
                if data_get["Percentage"] > 75:
                    print("the student details", data_get)
                    count += 1
            except EOFError:
                pass
                break
    return "the no of students got above 75", count


print(count_rec())





