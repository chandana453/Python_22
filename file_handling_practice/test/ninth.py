import os.path
import re

path = "C:\\Users\\Dell\\OneDrive\\Desktop\\fourth.txt"
# path = "../text_file/fourth.txt"

def hash_display(path):
    if os.path.exists(path) is True:
        f = open(path, "r")
        e = []

        list_of_lines = f.read()
        list_of_lines2 = re.sub(r"[.,]", "", list_of_lines)
        words = list_of_lines2.split(" ")
        for word in words:
            for char in word:
                e.append(char)
            e.append(" ")
        f.close()
        return " # ".join(e)
    else:
        return  "file not found"

val = hash_display(path)
print(val)