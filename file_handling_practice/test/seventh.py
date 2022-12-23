import os.path
import re

path = "C:\\Users\\Dell\\OneDrive\\Desktop\\fourth.txt"
# path = "../text_file/fourth.txt"

def words_ending_with_e(path):
    if os.path.exists(path) is True:
        f = open(path, "r")
        list_of_lines = f.read()
        list_of_lines2 = re.sub(r"[.,]", "", list_of_lines)
        words = list_of_lines2.split(" ")
        count = 0
        for word in words:
            if word[-1] == "e":
                count += 1
        f.close()
        return count
    else:
        return "file not found"


val = words_ending_with_e(path)
print(val)