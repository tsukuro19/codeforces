def Solution():
    n=int(input())
    a=list(map(int,input().split(' ')))
    count=1
    final=1
    i=0
    a.sort()
    while i<(n-1):
        if a[i]==a[i+1]:
            count=count+1
            i=i+1
            if final<count:
                final=count
            continue
        count=1
        i=i+1
    print(n-final)

t=int(input())
while(t!=0):
    Solution()
    t-=1