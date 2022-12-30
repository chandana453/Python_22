import csv

# read flash.dat to a list of lists
datContent = [i.strip().split() for i in open("./players.dat").readlines()]
print(datContent)
# write it as a new CSV file
with open("./flash.csv", "wb") as f:
    writer = csv.writer(f)
    print(writer)
    writer.writerows(datContent)