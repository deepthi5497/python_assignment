# def computeGCD(x, y):
#     if x > y:
#         small = y
#     else:
#         small = x
#     for i in range(1, small + 1):
#         if (x % i == 0) and (y % i == 0):
#             gcd = i
#
#     return gcd
#
#
# a = 60
# b = 48
# print ("The gcd of 60 and 48 is : ")
# print (computeGCD(60, 48))

def gcd1(a,b):
    if (b==0):
        return a
    else:
        return gcd1(b,a % b)


a = int(input("enter a number"))
b = int(input("enter second number"))
print("The gcd of given numbers is : ")
print(gcd1(a,b))

