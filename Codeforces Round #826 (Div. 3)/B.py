def Solution(n):
    a=[]
    b=[]
    if n==3:
        print(-1)
    else:
        for i in range(3,n+1):
            print(i,end=' ')
        print(2,1)
t=int(input())
while t!=0:
    n=int(input())
    Solution(n)
    t-=1