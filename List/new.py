# list = [1,2,4,5,2,"hello ",]
# print(list)
# for i in range(len(list)):
#     print(list[i],end=" ")


# creat empty list
# list=[]
# list1=list
# print(list)
# print(list1)
# properties 
# 1.mutable
# 2.dynamic in size
# 3.mixed data type
# 4.
list =eval(input("enter the list"))
print(type(list))
#  wap totake int from user and increse all t even by 5 and decrese all the odd num by 5
for i in range(len(list)):
    if list[i]%2==0:
        list[i]+=5
    else:
        list[i]-+5

print(list)
