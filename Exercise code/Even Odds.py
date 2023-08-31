n,k=map(int,input().split())
if n%2==0:
    if k<=(n//2):
        print(2*k-1)
    else:
        print((k-(n//2))*2)
else:
    temp=int(n/2)+1
    if k<=temp:
        print(2*k-1)
    else:
        print((k-temp)*2)