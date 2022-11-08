
print("Welcome to jaga of allipuram")
p=int(input("Enter your 4 digit pin number: "))
m = 20000

if(p == 1000):
    print("1-dobeysina dabulu")
    print("2-jobi lo dabulu Enquiry")
    print("3-lopala bayata cash")
    c = int(input("Please choose transactions: "))
    if (c == 1):
        w=int(input("Enter dobeysina amount: "))
        if (w < m and w%50 == 0):
            print("Please take your amount:", w)
        else:
            print("Invalid cash")

    elif (c==2):

        print("Your available amount : ",m)

    elif (c== 3):
        print("1->5,000")
        print("2->10,000")
        print("3->15,000")
        print("4->20,000")
        f = int(input("Enter lopala bayata cash option: "))
        if (f == 1 and 5000 < m):
            print("please take cash 5000")
        elif (f == 2 and 10000 < m):
            print("please take cash 10000")
        elif (f == 3 and 15000 < m):
            print("please take cash 15000")
        elif (f == 4 and 20000 < m):
            print("please take cash 20000")
        else:
            print("Invalid lopala bayata cash option")
    else:
        print("Wrong choice")
else:
    print("Wrong pin number")






