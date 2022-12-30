# Write a function in python to read the content from a text file "poem.txt" line by line and display the same on
# screen.

fo = open("poem.txt")

# try:
#     for i in fo.readlines():
#         print(i)
# except EOFError:
#     print("file not found")

class DataReading:

    @staticmethod
    def entire_data():
        return fo.read()

    @staticmethod
    def single_line():
        return fo.readline()

    @staticmethod
    def multi_lines():
        return fo.readlines()


obj1 = DataReading()
# print(obj1.entire_data())
print(obj1.single_line())
# print(obj1.multi_lines())


