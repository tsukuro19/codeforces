#https://codeforces.com/blog/entry/16736
n,m=map(int,input().split())
count=0
while n!=m:
    if(n<m):
        if m%2==0:
            m=m//2
            count+=1
        else:
            m+=1
            count+=1
    else:
        m+=1
        count+=1
print(count)
