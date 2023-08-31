n,h=map(int,input().split())
a=list(map(int,input().split()))
w=0
for i in range(n):
    if a[i]<=h:
        w+=1
    else:
        w+=2
print(w)