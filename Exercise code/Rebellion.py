#https://codeforces.com/blog/entry/108011
def rebelion(a,n):
    cmp=[[0]*(n+1),[0]*(n+1)]
    if sum(a)==0:
        print(0)
    elif all(i<j for i,j in zip(a,a[1:]))==True:
        print(0)
    else:
        for i in range(n):
            if a[i]==0:
                cmp[0][i+1]=cmp[0][i]+1
            else:
                cmp[0][i+1]=cmp[0][i]+0
            if a[i]==1:
                cmp[1][i+1]=cmp[1][i]+1
            else:
                cmp[1][i+1]=cmp[1][i]+0
        ans=n-1
        for last_zero in range(n+1):
            ans=min(ans,max(cmp[1][last_zero],cmp[0][n]-cmp[0][last_zero]))
        print(ans)


t=int(input())
while t!=0:
    n=int(input())
    a=list(map(int,input().split()))
    rebelion(a,n)
    t-=1