def count_pair(n,m):
    count=0
    for a in range(m+1):
        b=n-a**2
        if a+b**2==m and b>=0:
            count+=1
    return count

n,m=map(int,input().split())
print(count_pair(n,m))