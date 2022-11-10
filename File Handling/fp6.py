#6.Python Program to Count the Number of Words in a Text File

numbersOfWords=0

with open(r"myfile.txt","r") as file:
    data=file.read()
    #print(data)
    # Splitting the data into separate lines using the split() function
    lines=data.split()
    #print(lines)
    numbersOfWords+=len(lines) #adding the length of each line to the variable

print(numbersOfWords)
