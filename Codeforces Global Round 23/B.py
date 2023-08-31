def Solution(a,n):
    x,y=0,n-1
    count=0
    if all(i<j for i,j in zip(a,a[1:]))==True:
        print(0)
    else:
        while x<y:
            if a[x]==0 and a[y]==1:
                x+=1
                y-=1
            else:
                if a[x]==1:
                    if a[y]==1:
                        y-=1
                    else:
                        a[y]+=1
                        count+=1
                        a.remove(a[x])
                        if all(i<j for i,j in zip(a,a[1:]))==True:
                            break
                        else:
                            y-=1
                else:
                    if a[y]==1:
                        y-=1
                    else:
                        x+=1
        print(count)
                            


for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))[:n]
    Solution(a,n)