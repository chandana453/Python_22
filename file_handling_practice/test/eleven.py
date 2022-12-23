import pickle

path = "../text_file/book.dat"


def create_file(path):
    f = open(path, "ab")

    # [BookNo, Book_Name, Author, Price]
    book_no = int(input("enter the book no: "))
    Book_name = input("enter the book name : ")
    Author = input("enter the author name : ")
    Price = int(input("enter the price of Book : "))
    data = [book_no, Book_name, Author, Price]

    pickle.dump(data, f)

    f.close()


create_file(path)


def countRec(Author):
    count = 0
    with open(path, "rb") as f:
        try:
            while True:
                lst = pickle.load(f)
                print(lst)
                if Author == lst[2]:
                    count += 1
        except Exception:
            print("End Of File reached")
    return count


val = countRec("harshith")
print(val)
