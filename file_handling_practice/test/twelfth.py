#. Write a function count_rec() in Python that would read contents of the file "STUDENT.DAT" and display the details of those students whose percentage is above 75. Also display number of students scoring above 75%
import pickle

path ="../text_file/Student.dat"


## to add the student data into the student file

with open(path,"ab") as f:

    admission_num = int(input("enter asmission num: "))
    name = input("enter name : ")
    percentage = float(input("enter percentage"))

    data = [admission_num,name,percentage]
    pickle.dump(data,f)

##to calculate the total no of students whose percentage is greater than the entered percentage

def count_rec(per):
    with open(path,"rb") as f:
        try:
            count = 0
            while True:
                data = pickle.load(f)
                if data[2] > per:
                    count +=1
                    print(data)

        except Exception:
            print("End Of File is reached")

    print(f"the total no. of students having percentage greater than {per} is {count}")


percentage = float(input("enter a percentage : "))

count_rec(percentage)
