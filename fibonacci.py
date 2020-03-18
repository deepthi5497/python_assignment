def febo(number):
    if number in (0, 1):
        return number
    else:
        return febo(number - 1) + febo(number - 2)


for n in range(0, 10):
    print(febo(n))


# a = 0
# b = 1
# print(a)
# print(b)
# for i in range(1, 9):
#     c = a + b
#     a = b
#     b = c
#     print(c)

