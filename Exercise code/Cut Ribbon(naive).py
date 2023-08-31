n,a,b,c=map(int,input().split())
ans=0
for i in range(4001):
    for j in range(4001):
        rem=n-(a*i+b*j)
        if rem<0:
            break
        elif rem%c==0:
            ans=max(ans,(i+j+rem//c))
print(ans)