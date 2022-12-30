# Write a function in Python to count the words "this" and "these" present in a text file "article.txt".
# [Note that the words "this" and "these" are complete words]

fo = open("notes.txt", "r")

data = fo.read()

words = data.split()


def res():
    count = 0
    count1 =  0
    for i in words:
        if i == "this":
            count += 1
            if i == "these":
                count1 += 1
    return "the this word count",count, "the these word count",count1


print(res())




