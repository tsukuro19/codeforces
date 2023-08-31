t=int(input())
count=0
while t>0:
    p,q=map(int,input().split())
    if q-p>=2:
        count+=1
    t-=1
print(count)