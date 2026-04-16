# even index even num-1 odd index odd num+1
# mylist=[[6,8,9],[3,5,6],[9,2,6]]
# print(list)
a=/[0]
b=list[1]
c=list[2]
ans=[]
# for i in range(len(mylist)):
#     if(i%2==0):
#         temp=mylist[i].copy()
#         for j in range(len(mylist[i])):
#             if(j%2==0):
#                 temp
#                 # ans.append(mylist[j]-1)
#     else:
#         temp=mylist[i].copy()
#         for j in range(len(mylist[i])):
#             if(j%2!=0):
#                 ans.append(mylist[j]+1)

# print(ans)       i

mylist=[[6,8,9],[3,5,6],[9,2,6]]
print(list)
for i in range (len(mylist)):
    temp=mylist[i].copy()
    if i%2==0:
        for j in range (len(temp)):
            if temp[j]%2==0:
                temp[j]-=1
            ans.append(temp)
    else:
        for j in range(len(temp)):
            if temp[j]%2!=0:
                temp[j]+=1
            ans.append(temp)
print(ans)
