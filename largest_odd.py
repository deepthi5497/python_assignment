# x=int(input("enter number"))
# y=int(input("enter number"))
# z=int(input("enter number"))
# list1=[]
# if x%2!=0:
#     list1.append(x)
# if y%2!=0:
#     list1.append(y)
# if z%2!=0:
#     list1.append(z)
# # sorted=list1.sort()
# # print list1
# # print list1[-1:]
# max=0
# for i in list1:
#     if i>max:
#         max=i
# if max>0:
#     print max
# else:
#     print("no odd numbers")

"""#3.Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered.
#If no odd number was entered, it should print a message to that effect"""
# n=int(input("enter range"))
# list1=[]
# max=0
# for i in range(1,n+1):
#     element=int(input("enter numbers"))
#     if element%2!=0:
#         list1.append(element)
# print list1
# print list1
# for j in list1:
#     if j>max:
#         max=j
# if max>0:
#     print max
# else:
#     print "none are odd"


def getRatios(vect1,vect2):
    ratio=[]

    for i in range(0,len(vect1)):
        try:
            ratio.append(vect1[i]/(vect2[i]))
        except :
            ratio.append("invalid")

    return ratio

ratio1=[1,2,3,4,5]
ratio2=[6,7,8,9,0]
res=getRatios(ratio1,ratio2)
print(res)