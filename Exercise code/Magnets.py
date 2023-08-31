n=int(input())
list_magnet=[]
while n>0:
    magnet=input()
    list_magnet.append(magnet)
    n-=1
temp,count=list_magnet[0],1
for i in range(1,len(list_magnet)):
    if temp!=list_magnet[i]:
        temp=list_magnet[i]
        count+=1
print(count)