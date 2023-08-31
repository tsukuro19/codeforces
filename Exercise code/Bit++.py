n=int(input())
count=0
for i in range(n):
    t=input()
    if t[1]=='+':
        count+=1
    else:
        count-=1
print(count)