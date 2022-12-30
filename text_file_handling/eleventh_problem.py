# A binary file "Book.dat" has structure [BookNo, Book_Name, Author, Price].
# i. Write a user defined function createFile() to input data for a record and add to Book.dat.
# ii. Write a function countRec(Author) in Python which accepts the Author name as parameter and count and return
# number of books by the given Author are stored in the binary file "Book.dat
#
import pickle


def createfile():
    # data = {"BookNo": 1, "Book_Name": "chirajeevi", "Author": "Megastar", "Price": 450}
    # data = {"\nBookNo": 2, "Book_Name": "pawankalyan", "Author": "powerstar", "Price": 450}
    # data = {"\nBookNo": 3, "Book_Name": "ramcharan", "Author": "Megastar", "Price": 650}

    # data = [1, "Chiranjeevi", "Megastar", 450]
    # data = ["2", "ramacharan", "Megastar", 550]
    data = ["3", "PAWANKALYAN", "Powerstar", 350]

    fo = open("book.dat", "ab")

    pickle.dump(data, fo)

    return "ok done"


def countrec(Author):
    with open("players.dat", "rb") as file:
        count = 0
        # data = pickle.load(file)
        # print(data)
        while True:
            try:
                data = pickle.load(file)
                print(data)
                # if data[2] == Author:
                #     count += 1
            except EOFError:
                pass
                break
    return "the count of author repeated", count


# print(createfile())
res = countrec("Powerstar")
print(res)

print(res)
