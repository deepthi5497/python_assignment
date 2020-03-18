string1=raw_input("enter string: ").lower()
list1=[]
for i in string1:
    if i not in list1:
        if i!=" ":
            list1.append(i)
print(list1)
if len(list1)==26:
    print("pangram")
else:
    print("not")