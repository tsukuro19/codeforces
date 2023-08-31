from math import sqrt

def check_t_primes(t):
    count=2
    if t==1:
        print("NO")
    else:
        for i in range(2,t):
            if (t%i)==0:
                count+=1
        if count==3:
            print("YES")
        else:
            print("NO")

n=int(input())
t=list(map(int,input().split()))
for i in range(len(t)):
    check_t_primes(t[i])