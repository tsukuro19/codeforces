n,m,a,b=map(int,input().split())
result=0
if m*a<=b:
    print(a*n)
else:
    result=(n//m)*b+min((n%m)*a,b)
    print(int(result))
