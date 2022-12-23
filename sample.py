# def add(a,b):
#     'adding'
#     return a+b
#
# print(add.__doc__)   # to print docstring
#
# __A=10
# print(__A)
#
#
# name="Mounika"
# DOB="2602"
# State="TG"
# print(f'Hey, I am {name} and my dob is {DOB} and my state is {State}')
#
#
# a=(2+3j)
# print(a)
#
# l=[1,2,3]
# t=(4,5)
# #l.extend("abc")
# l.extend("def")
# print(l)
#
# lst=[[1,2],[3,4],6,7,'a']
#
# for sub_list in lst:
#     print(sub_list)
#     #print(sub_list[0])
#
# l=[1,2,3,4,5,6,7,8,9,10]
# print(l[::11])
#
# d={'a':1,'b':2,'c':3}
# d.update({'a':10})
# print(d)

#d.get(e) # doesn't return error returns none
#d['e'] # gives key error

# d={(1,2,3):'a'}   # tuple can be used as a key in dict (bcoz tuple is immutable)
# d={(1,2,[3,4]):'a'}  # ERROR :unhashable type: 'list' ,bcoz key is unique and lists are immutable
# print(d)


# s="I am Hari,TTT am,hari"
# s= s.replace(',',' ')
# new_str=s.lower().split(' ')
# print(new_str)
# d={}
# for word in new_str:
#     if word in d:
#         d[word]+=1
#     else:
#         d[word]=1
#
# print(d)

# import re
# s="I am Hari,TTT am, hari"
# s=re.findall(r"\w+",s.lower())
# d={}
# for word in s:
#     if word in d:
#         d[word]+=1
#     else:
#         d[word]=1
#
# print(d)



# def solution(year):
#     if (year % 100) == 0:
#         return (year) // 100
#     else:
#         return (year) // 100 + 1
#
# solution(2001)



#
# a = int(input('Find the Century = '))
# #Divide the number by 100
#
# century = a // 100
# #Check if the year belongs the same century
#
# if(a%100 != 0):
#       century = century + 1
# print(century)

# input_st="ab"
# #rev=input_st[::-1]
# rev=input_st.reverse()
# if rev==input_st:
#     print("T")
# else:
#     print("F")

# inputArray = [3, 6, -2, -5, 7, 3]

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

#
# a=[1,"None",2,"None","None",3,"None"]
# for i in a:
#   if a[i] is "None":
#     a[i]=a[i-1]
#
# print(a)


x =[None, None, 1, 2, None, None, 3, 4, None, 5, None, None]
for i,e in enumerate(x[:-1], 1):
    if x[i] is None:
        x[i] = x[i-1]
print(x)




#output = "2a 2b 1c 2d 1a"
# new_str=input.strip()
# d={}
#
# for i in new_str:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
#
# print(d)








