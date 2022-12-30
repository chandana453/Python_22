# Write a function AMCount() in Python, which should read each character of a text file STORY.TXT,
# should count and display the occurrence of alphabets A and M (including small cases a and m too).
# For Example:
# If the file content is as follows:
# Updated information
# As simplified by official websites.
# The EUCount() function should display the output as:
# A or a:4
# M or m :2

fo = open("example.txt", "r")

data = fo.read()

output = {}


def AMcount():
    count = 0
    count1 = 0
    for i in data:
        if i[0] == "A" or i[0] == "a":
            count += 1
        elif i[0] == "M" or i[0] == "m":
            count1 += 1
    res1 = "A or a:", count
    res2 = "M or m:", count1
    return res1, res2


print(AMcount())





