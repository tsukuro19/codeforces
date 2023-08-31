k,n,w=map(int,input().split())
sum_lend=0
for i in range(1,w+1):
    sum_lend+=k*i
if n-sum_lend<0:
    print(abs(sum_lend-n))
else:
    print(0)