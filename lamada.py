# x=int(input("enter"))
# res=lambda x:x%10
# print(res(x))

# x=int(input("enter"))
# res=lambda x:x*x*x
# print(res(x))

# str1={'a','b',"c"}
# # res=list(map(lambda x:x+"a",str1))
# # print(res)
# #
# # str1=[1,2,3,4,5,6,7]
# # res=list(filter(lambda x:x%2==0,str1))
# # print("even:",res)
# # res1=list(filter(lambda x:x%2!=0,str1))
# # print("odd:",res1)

my_list = [1, 3, 6, 10]
print next(x**2 for x in my_list)


list1=[1,2,3,4,5,6,7,8,9,10]
res=map(lambda val:val**2,list1)
print res
