# list=[7,8293,7,-8,-2,89,-34,93,90]
# print(list[1:9:3])
# print(list[:-5:-10])
# # delete 
# # ADD ELEMENET 
# list.append("hellloo")
# print(list)

# list.insert(3,10)
# print(list)
# list1=[78,9983,3784]
# # list.extend(list1)
# list+=list1   #extend 
# print(list)

# last=[5,3,2,1,4,8]
# total=sum(last)
# print(total)
# ans=[]
# for i in last:
#     ans.append(total-i)
# print(ans)
# ans=[18, 20, 21, 22, 19, 15]

# total=sum(last)
# print(total)
# for i in range(len(last)):
#     print(last[total-i],end=" ")

# list=[[1,3,5,6],[4,5,7,4],[7,3,9,2],[8,47,73,7]]
# d=list[0]
# a=list[1]
# b=list[2]
# c=list[3]
# print(sum(d))
# print(sum(a))
# print(sum(b))
# print(sum(c))



# # total=sum(list)
# # print(total)

# a=lst

list=[[1,3,5,6],[4,5,7,4],[7,3,9,2],[8,47,73,7]]

ans=[]
for i in range(len(list)):
    temp=0
    for j in list[i]:
        temp+=j
    ans.append(temp)
print(ans)
