# Write a function display_words() in python to read lines from a text file "story.txt", and display those words,
# which are less than 4 characters.

fo = open("notes.txt", "r")

data = fo.read()

words = data.split()


def res():
    for i in words:
        if len(i) < 4:
            print(i)


print(res())
