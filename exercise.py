import csv
with open("sample.csv", 'r')as fh:
    avg = 0
    res = csv.reader(fh)
    list1 = list(res)
    dict1 = {}
    for row in list1[1::]:
        sum1 = 0
        n = 0
        for marks in row:
            if marks.isdigit():
                n += 1
                sum1 = sum1 + int(marks)
        avg = sum1/n
        dict1[row[0]] = ["sum: ", sum1, "avg: ", avg]
    print(dict1)
    a = {}
    rank1 = 0
    for i in sorted(dict1, key=dict1.get, reverse=True):
        rank1 += 1
        a[i] = rank1
    print("ranks: ", a)

    # c=sorted(dict1, key=itemgetter(1), reverse=True)
    #
    # # for i in enumerate(sorted(dict1, key=itemgetter(1), reverse=True)):
    # #     print(dict1[i])

"""difference between two dictionaries and the count of common values in a dictionary"""
# dict1 = {'a': 10, 'b': 11}
# dict2 = {'a': 10, 'k': 13, 'c': 3}
# dict3 = {}
# for i in dict1:
#     if i not in dict2:
#         dict3[i] = dict1[i]
#     if i in dict2:
#         dict3[i] = dict1[i]+dict2[i]
# for i in dict2:
#     if i not in dict1:
#         dict3[i] = dict2[i]
# print(dict3)

# value = set(dict1)^set(dict2)
# print(value)
# res=set(dict1)
# print(res)




