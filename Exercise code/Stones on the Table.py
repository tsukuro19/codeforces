n=int(input())
stone=input()
temp=stone[0]
count=0
for i in range(1,len(stone)):
    if stone[i]==temp:
        count+=1
    temp=stone[i]
print(count)