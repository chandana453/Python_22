a=10
b=15
print(a) if a>b else print("=") if a==b else print(b)


print("......NESTED IF......")
x=30
if x>10:
    print("x is greater than 10")
    if(x>20):
        print("x is also greater than 20")
    else:
        print("not greater than 20")

print(".....while loop....")
i=0
while i<6:
    print(i)
    if i==3:
        break
    i+=1

#With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Note that number 3 is missing in the result

# Print a message once the condition is false.
print("loop with msg")
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# Example
# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

#The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#The "inner loop" will be executed one time for each iteration of the "outer loop":
print("....NESTED LOOPS....")
adj=["red","big","tasty"]
fruits=["banana","apple","cherry"]
for i in adj:
    for j in fruits:
        print(i,j)