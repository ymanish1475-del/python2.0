print(5**5);
# def na
# wap which take a num as input from userif the num is even it will calculate even factoril and odd factorial

# n = input("enter n = ")
# if(n%2==0){
#     print

# }else{

# }
# n=input("enter=")
# if a%2==0:
#     def factor(n):
#         for i in range(1,n+1):
#             if n%i==0:
#                 print(i,end=" ")
# # factor(12)       
# else:
#     def factor(n):
#         for i in range(1,n+1):
#             if n%i==1:
#                 print(i,end=" ")
def evenf(n):
    ans=1
    for i in range(2,n+1,2):
        ans=ans*i
    return ans

def oddf(n):
    ans=1
    for i in range(2,n+1,)
