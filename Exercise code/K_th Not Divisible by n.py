t=int(input())
while(t>0):
    n,k=map(int,input().split())
    print(k+((k-1)//(n-1)))
    t-=1