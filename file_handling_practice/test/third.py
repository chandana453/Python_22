import os.path

path = "C:\\Users\\Dell\\OneDrive\\Desktop\\fourth.txt"
# path = "../text_file/fourth.txt"


def word_count(path):
    count = 0
    if os.path.exists(path) is True:
        f= open(path,"r")
        list_of_file = f.read()
        words = list_of_file.split(" ")
        for word in words:
            count += 1
        f.close()
        return count
    else:
        return "file not found"


print(word_count(path))