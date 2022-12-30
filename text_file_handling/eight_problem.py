# Write a function in Python to count uppercase character in a text file.

fo = open("notes.txt", "r")

data = fo.read()


def res():
    count = 0
    for letter in data:
        if letter.isupper():
            count += 1
    return count


print(res())
