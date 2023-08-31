a,b=map(int,input().split())
count=0
if a==b:
    print(1)
else:
    while a<=b:
        a*=3
        b*=2
        count+=1
    print(count)