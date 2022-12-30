# Write a function in Python to count words in a text file those are ending with alphabet "e"

fo = open("notes.txt", "r")

data = fo.read()

words = data.split()


def res():
    count = 0
    for i in words:
        if i[-1] == "e":
            count += 1
    return count


print(res())
