# Write a function to search and display details of student whose rollno is '1005'
# from the binary file student.dat having structure [rollno, name, class and fees]
# A binary file school.dat has structure(rollno, name, class, fees)
# Write a definition for function total_fees( ) that reads each object of file and
# calculate the total fees of students and display the same.

import pickle


def data_add():
    data_input = {"rollno": 1005, "name": "muthu", "class": "8th", "fees": 20000}
    with open("students.dat", "ab") as file:
        pickle.dump(data_input, file)
    return "ok done"

# print(data_add())


def details_of_student(rollno):
    with open("students.dat", "rb") as file1:
        while True:
            try:
                data = pickle.load(file1)
                print(data)
                if data["rollno"] == rollno:
                    return "the student details", data
            except EOFError:
                print("the details not exist for the rollno")


# print(details_of_student(1005))


def total_fees():
    with open("students.dat", "rb") as file2:
        fees1 = []
        while True:
            try:
                data1 = pickle.load(file2)
                # print(data1)
                # print(data1["fees"])
                fees1.append(data1["fees"])
            except EOFError:
                pass
                break
    return "the total fees of the students", sum(fees1)


print(total_fees())




