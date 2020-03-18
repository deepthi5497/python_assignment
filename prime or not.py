# num = int(input("enter number"))
# for i in range(2, num):
#     if num % i != 0:
#         if i == num-1:
#             print("prime")
#         else:
#             continue
#     else:
#         print("not prime")
#         break


num = int(input("enter number"))
count = 0
list1 = []
for i in range(1, num+1):
    if num % i == 0:
        list1.append(i)
        count = count+1
    else:
        continue
if count == 2:
    print("prime", list1)
else:
    print("not prime")
