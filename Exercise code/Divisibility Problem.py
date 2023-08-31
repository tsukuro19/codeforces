t=int(input())
while t>0:
    a,b=map(int,input().split())
    if a<b:
        print(b-a)
    elif a%b==0:
        print(0)
    else:
        print(b-a%b)
    t-=1