import os.path

path = "C:\\Users\\Dell\\OneDrive\\Desktop\\fourth.txt"
# path = "../text_file/fourth.txt"

def AM_counter(path):
    if os.path.exists(path) is True:
        f = open(path,"r")
        list_of_lines = f.read()
        words = list_of_lines.split(" ")
        c_A = 0
        c_M = 0
        for word in words:
            for char in word:
                if char.upper() == "A":
                    c_A += 1
                if char.upper() == "M":
                    c_M += 1
        f.close()
        return f"A or a : {c_A} , \n M or m : {c_M} "

val = AM_counter(path)
print(val)