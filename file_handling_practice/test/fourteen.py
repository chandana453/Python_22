# Write a function to search and display details of student whose rollno is '1005' from the binary file student.dat having structure [rollno, name, class and fees]
#
#
# A binary file school.dat has structure(rollno, name, class, fees)
#
# Write a definition for function total_fees( ) that reads each object of file and calculate the total fees of students and display the same.



import pickle

path = "../text_file/school.dat"



##to append details into file
with open(path,"ab") as stu_data_file:

    roll_num = int(input("enter roll num: "))
    name = input("enter name : ")
    class_no =int(input("enter the class : "))
    fee = float(input("enter fee details"))
    data = {'roll_num' : roll_num ,'name' : name ,'class_no' : class_no ,'fee': fee}
    pickle.dump(data,stu_data_file)


## to display student details whose rool no matches with the requested roll no
def stu_display(roll_no):
    with open(path, "rb") as f:
        try:
            count = 0
            while True:
                data = pickle.load(f)
                if data["roll_num"] == roll_no:
                    print(data)
        except Exception:
            print("end of the file")

roll = int(input("enter the roll_no to display : "))
stu_display(roll)



##to calculate the total fee
def total_fees():
    try:
        with open(path,"rb") as sch_file:
            fee = 0
            while True:
                data = pickle.load(sch_file)

                fee += data["fee"]
                print(fee)
    except Exception:
        print("end of the file")


total_fees()

