k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
count=d
if k==1 or l==1 or m==1 or n==1:
    print(d)
else:
    for i in range(1,d+1):
        if i%k!=0 and i%l!=0 and i%m!=0 and i%n!=0:
            count-=1
    print(count)