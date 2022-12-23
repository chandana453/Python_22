# Given a binary file employee.dat, created using dictionary object having keys: (empcode, name, and salary)
#
# Write a python function that add one more record at the end of file.
# Write a python function that display all employee records whose salary is more that 30000
import pickle


path = "../text_file/emp.dat"


##to add emp data into emp file

def add_emp_data():
    with open(path,"ab") as emp_file:
         emp_code = int(input("enter the emp code : "))
         name = input("enter the name : ")
         salary = float(input("enter the salary : "))
         data = {"emp_code" : emp_code, "name": name, "salary": salary}
         pickle.dump(data,emp_file)


add_emp_data()



##to display the details of emp whose salary is greater than the entered salary

def display(sal):
    with open(path,"rb") as emp_file:
         try:
              while True:
                  data = pickle.load(emp_file)
                  if data["salary"] > sal:
                      print(data["name"])
         except Exception:
             print("end of the file")
sal = float(input("enter salary to check : "))
display(sal)