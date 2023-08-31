n=int(input())
a=sorted(list(map(int,input().strip().split())))
count=0
sum_coin=0
x=sum(a)
while sum_coin<=sum(a):
    sum_coin+=a.pop()
    count+=1
print(count)