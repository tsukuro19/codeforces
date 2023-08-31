x=int(input())
move=[1,2,3,4,5]
count=0
while x!=0:
    if x>=max(move):
        x-=max(move)
        count+=1
    else:
        move.remove(max(move))
print(count)