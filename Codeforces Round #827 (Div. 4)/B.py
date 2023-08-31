def Solution(a):
    a_sorted=sorted(a)
    check=all(i<j for i,j in zip(a_sorted,a_sorted[1:]))
    if len(a)==1:
        print('YES')
    else:
        if check==True:
            print("YES")
        else:
            print('NO')

t=int(input())
while t!=0:
    n=int(input())
    a=list(map(int,input().strip().split()))[:n]
    Solution(a)
    t-=1