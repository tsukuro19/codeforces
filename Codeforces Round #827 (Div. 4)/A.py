def Solution(a):
    a_sorted=sorted(a)
    if sum(a)==0:
        print('YES')
    else:
        if a_sorted[0]+a_sorted[1]==a_sorted[2]:
            print('YES')
        else:
            print('NO')

t=int(input())
while t!=0:
    a=list(map(int,input().strip().split()))[:3]
    Solution(a)
    t-=1