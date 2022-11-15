#4.Define a list that contains the marks percentage for the students. Print a list that contains the Grades of the students.
  # The grading will be decided by the following conditions.
  # A+ if the percentage is greater than 90
  # A if the percentage is less than or equal to 90 and greater than 70
  # B if the percentage is less than or equal to 70 and greater than 50
  # C if the percentage is less than or equal to 50 and greater than 35
  # F if the percentage is less than or equal to 35

marks_list=[97, 95, 96, 98, 89, 95]

max_marks = len(marks_list) * 100

total = 0

for i in range(len(marks_list)):
    total += marks_list[i]

percentage = ((total) / max_marks) * 100

if percentage >= 90:
    grade = 'A+'

elif percentage <= 90 and percentage > 70:
    grade = 'A'

elif percentage <= 70 and percentage > 50:
    grade = 'B'

elif percentage <=50  and percentage > 35:
    grade = 'C'

else:
     grade = 'F'

print(grade)

