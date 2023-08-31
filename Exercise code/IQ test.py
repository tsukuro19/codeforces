n=int(input())
even,odd=0,0
a=list(map(int,input().split()))
for i in range(n):
    if a[i]%2==0:
        even+=1
    else:
        odd+=1
for i in range(n):
    if (even==1 and a[i]%2==0) or (odd==1 and a[i]%2!=0):
        print(i+1)
        break