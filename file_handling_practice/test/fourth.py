import os.path

path = "C:\\Users\\Dell\\OneDrive\\Desktop\\fourth.txt"
# path = "../text_file/fourth.txt"


if os.path.exists(path) is True:
    f = open(path,"r")
    list_of_lines = f.read()
    words = list_of_lines.split(" ")
    print(words.count("the"))
    f.close()










