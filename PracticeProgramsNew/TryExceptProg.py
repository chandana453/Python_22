#2.Write a python program with buggy code and add a try/except clause so the code runs without errors.

list1=[1,3,4,5,2,1,0,2,5,0,13,45,23,12]

new_list=[]

for num in range(len(list1)):
    try:
      if 5%list1[num]==0:
         new_list.append(list1[num])
    except ZeroDivisionError:
        print("Divide by Zero not possible")
        new_list.append("DivideByZero")
    finally:
        print("Operation Performed")

print(new_list)

#2nd example
full_lst = ["ab", 'cde', 'fgh', 'i', 'jkml', 'nop', 'qr', 's', 'tv', 'wxy', 'z']

result = []

for ele in full_lst:
    try:
        result.append(ele[1])  # adding each element of index 1 to the result
    except IndexError:
        result.append("Error")

print(result)
