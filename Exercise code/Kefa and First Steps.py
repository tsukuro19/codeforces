n=int(input())
moneys=list(map(int,input().split()))
max_len,current=1,1
for i in range(1,n):
    if moneys[i]>=moneys[i-1]:
        current+=1
    else:
        if max_len<current:
            max_len=current
        current=1
if current>max_len:
    max_len=current
print(max_len)