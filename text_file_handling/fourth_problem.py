# Write a function in Python to read lines from a text file "notes.txt".
# Your function should find and display the occurrence of the word "the".

fo = open("notes.txt", "r")

occ_the = fo.read().split()


def res(x):
    gh = 0
    count = 0
    jk ={}
    for i in occ_the:
        if x == i:
            # print(i)
            gh += 1
        else:
            count += 1
            jk[i] = count

    return


print(res("the"))
