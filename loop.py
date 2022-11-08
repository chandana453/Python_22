# formatted strings
import math
word = 'practise sustainability'
print(word.upper())
print(word.find('s'))
print(word.replace('sustainability','SUSTAINABILITY'))
print(word.title())
print(math.ceil(3.1))

#CONDITIONS
is_prices_high = False
is_prices_low = False
if is_prices_high :
    print("check your usages")
elif is_prices_low:
    print("the prices are decreased")
else :
    print("look at your expensives")
print("Happy shopping")
"""

#problem1
is_service = int(input('experience in firm? '))
salary = int(input('salary '))
bonus = salary * 0.05
if is_service > 5 :
    print(bonus)
else :
    print("increase your experience")
# problem 2
length = int(input('the length of rectangle? '))
breadth = int(input('the breadth of rectangle? '))
is_square = length == breadth
if is_square :
    print("it is square")
else :
    print("it is not square")
# problem 3
a = int(input('value for a '))
b = int(input('value for b '))
if a > b :
    print(a)
elif b > a:
    print(b)
else :
    print("both are equal")
# problem 4
quantity = int(input("the quantity required? "))
cost_of_product = quantity * 100
discount = cost_of_product-cost_of_product*0.1
if quantity > 1000 :
    print(discount)
else :
    print("no discount")

# problem 5
marks = int(input("the marks of person? "))
if marks < 25:
    print("F")
elif  marks >=25 and marks < 45:
    print("E")
elif marks >=45 and marks < 50:
    print("D")
elif marks >=50 and marks < 60:
    print("C")
elif marks >=60 and marks < 70:
    print("B")
else:
    print("A")

# problem 6
a = int(input("age of  a? "))
b = int(input("age of b? "))
c = int(input("age of c? "))
if a>b and a>c :
    print("a is older")
elif b>a and b>c :
    print("b is older")
elif c>a and c>b :
    print("c is older")
else :
    print("all are equal")

# problem 7
input_value = int(input("the input value? "))
if input_value < 0 :
    print(input_value *- 1)
else :
    print(input_value)
print(abs(input_value))

#problem 8
number_of_classes_held = int(input("the number of classes held? "))
number_of_classes_attended = int(input("the number of classes attended? "))
percentages_of_classes = (number_of_classes_attended /number_of_classes_held ) * 100
if percentages_of_classes < 75 :
    print(percentages_of_classes)
    print("he will not allowed to sit in the class")
else :
    print("he will be allowed")

#problem 9
number_of_classes_held = int(input("the number of classes held? "))
number_of_classes_attended = int(input("the number of classes attended? "))
percentages_of_classes = (number_of_classes_attended /number_of_classes_held ) * 100
health_problem = input("is there health  problem? ")
if percentages_of_classes < 75 and health_problem :
    print(percentages_of_classes)
    print("he will BE allowed to sit in the class")
else :
    print("he will be allowed")

price = 1000000
buyer_salary = input("is buyer has good credit? ")
if buyer_salary :
    down_payment = price * 0.1
else :
   down_payment  = price * 0.2
print(f"Down payment: ${down_payment}")
# WEIGHT CONVERTER
weight = int(input("< "))
units = input("(L)bs or (K)g: ")
if units.upper()== "L" :
    print(weight * 0.46)
else:
    print(weight / 0.46)
 
# while loop
n = int(input("< "))
counter = 0
while counter < n :
    print('* ' * n)
    counter = counter + 1
print("break")
a = True
i = 1
while a :
    if i >3 :
        a = False
    i= i + 1
print(i)

# print individual characters
word = input("the input ")
length_of_word = len(word)
counter = 0
while counter <= (length_of_word)-1 :

    print(word[counter])
    counter = counter + 1
# right angle triangle
n = int(input("< "))
counter = 1
while counter <= n :
    print("* " * counter)
    counter+=1
"""
# for lopp

for each_number in range(9):
    print(each_number)
total = 99
for i in range(1,1):
    total =total + 2
print(total)
number ="1234"
for digit in str(number):
    print(digit)
slogan = "save earth, save lives"
length_of_slogan = len(slogan)
for i in range(length_of_slogan):
    if slogan[i] == " " :
        print(slogan[:i])
word = "save earth make your lives better"
length_of_word = len(word)
for i in range(length_of_word):
    if word[i] == " " :
        print(word[0:i])
sport = "foot ball"
for i in range(len(sport)) :
    print(i)
number =20
for i in range(number):
    number = number-1
print(number)
#count of a number

n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)
list = [1,7,2,8,3,9,4]
list.sort()
print(list)
#format string
age = 26
name = "my name is sailajesh and i am {}"
print(name.format(age))



