
# wap

dt={1:3,4:5,5:8,4:8,12:6}
ans=0;
for k,v in dt.items():
    if 12%v==0:
        ans+=k

print(ans)