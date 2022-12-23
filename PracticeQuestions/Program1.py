#1. input ="aabbcdda" output="2a 2b 1c 2d 1a"

# s = "aabbcdda"
# new_s=""
# count=1
# for i in range(len(s)-1):
#     if s[i]==s[i+1]:
#         count=count+1
#     else:
#         new_s+=str(count)+s[i]+" "
#         count=1
#
# new_s+= str(count)+s[-1]
# print(new_s)

#2.input=[1,"None",2,"None","None",3,"None"],output=[1,1,2,2,2,3,3]
# input=[1,"None",2,"None","None",3,"None"]
# lst=[]
# previous= None
# for i in input:
#     if i=="None":
#         lst.append(previous)
#     else:
#         previous = i
#         lst.append(i)
#
# print(lst)

#3.input ="abaacbe" output =3

# def del_characters(st,i,j):
#     if(i >= j):
#         return 0
#     if(st[i]==st[j]):
#         return del_characters(st,i+1,j-1)
#     # Return value, incrementing by 1...return minimum Element between two values
#     return (1+ min(del_characters(st,i+1,j),del_characters(st,i,j-1)))
#
# s ="abaacbe"
# def min_ele_del(Str):
#     # Utility function call
#     return del_characters(s,0,len(s)-1)
#
# print("Minimum element of deletions =",min_ele_del(s))

#4. input a=[1,2,3,4], b=[5,6,7] output =[6,8,10,4]

# a=[1,2,3,4]
# b=[5,6,7]
# out=[]
#
# for i in range(len(a)):
#   if i<len(a)
#     out.append(a[i]+b[i])
#   if i<len(a):
#   #     out.append(a[i])
#   # else:
#   #     out.append(b[i])

# print(out)

import numpy as np
# A=[1,2,3,4]
# B=[5,6,7]
# a=np.array(A)
# b=np.array(B)
# b.resize(a.shape)
# c=a+b
# print(list(c))

#5.input = "This is the automation" output=["is is the automation","is the automation","ion"]
# input = "This is the automation"
# lst=[]
# for word in input:
#     input.split("i")


inputArray = [-1,-2,0,5,6]
# res = 1
# max = min(inputArray)
# # if len(inputArray)==1:
# #     print(max)
# for i in range(len(inputArray)-1):
#     res = inputArray[i] * inputArray[i+1]
#     if res > max:
#         max = res
# print(max)


# result=[inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)]
# print(max(result))


sequence=[1,3,2]
count=0
# for i in range(len(sequence)-1):
#     if sequence[i]>sequence[i+1]:
#         count+=1
#         if sequence[i-1]<=sequence[i+1]:
#             print(False)
#
# if count<=1:
#     print(True)


# a= [-120, -120]
# #a=[1,2,3,1]
# d = {}
# for i in range(len(a)):
#     a[i]=abs(a[i])
#     if a[i] not in d:
#         d[i] = a[i]
#     else:
#         print(True)

#print(False)


def main():
    f = open("guru99.txt", "w+")
    # f=open("guru99.txt","a+")
    for i in range(10):
        f.write("This is line %d\r\n" % (i + 1))
    f.close()
    # Open the file back and read the contents
    f=open("guru99.txt", "r")
    if f.mode == 'r':
        contents =f.read()
        # print contents or, readlines reads the individual line into a list
    fl =f.readlines()
    for x in fl:
     print(x)


if __name__ == "__main__":
    main()


#
# def main():
#     f = open("guru99.txt", "w+")
#     # f=open("guru99.txt","a+")
#     for i in range(10):
#         f.write("This is line %d\r\n" % (i + 1))
#     f.close()
#     # Open the file back and read the contents
#     # f=open("guru99.txt", "r")
#     # if f.mode == 'r':
#     #   contents =f.read()
#     #    print (contents)
#     # or, readlines reads the individual line into a list
#     # fl =f.readlines()
#     # for x in fl:
#     # print(x)
#
#
# if __name__ == "__main__":
#     main()

