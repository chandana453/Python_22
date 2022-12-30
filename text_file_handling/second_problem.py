# Write a function in python to count the number of lines
# from a text file "example.txt" which is not starting with an alphabet "G"
# def count_letter(x):
#     count = 0
#     fo = open("example.txt")
#     lst = fo.readlines()
#     for i in lst:
#         if i[0] != x:
#             count += 1
#     return "So for number of sentences which is not starts with G: ", count
#
#
# print(count_letter("G"))

fo = open("example.txt")

words = fo.read().split()

res = len(words)

print(words, res)
