"""remove space"""
# str1="hello world"
# print(str1.replace(" ",""))

"""reversing a list"""
# list1=[1,2,3,4,5]
# print(list1[::-1])
# print(list(reversed(list1)))

"""list to string and string to list"""
# print(str1.split(""))

"""removing of duplicates from string"""
# list1=[1,2,3,1,2,3,5]
# a=list(set(list1))
# print(a)
# b=set(list1)
# print(b)
# print(list1.pop())

a1 = ['C', 'I', 'G', 'N', 'A', 'I', 'L', 'C', 'A','I',]
s1 = 'CIGNA'


def f(a, s):
    j = 0
    for i in range(0, len(a)-1):
        if a1[i] == s1[j] and i >= j:
            print(a[i], i)
            j += 1
    if j == len(s1):
        return True
    else:
        return False


print(f(a1, s1))

