n=int(input())
sum_coordinate=[0,0,0]
for i in range(n):
    x,y,z=map(int,input().split())
    sum_coordinate[0]+=x
    sum_coordinate[1]+=y
    sum_coordinate[2]+=z

if sum_coordinate[0]==0 and sum_coordinate[1]==0 and sum_coordinate[2]==0:
    print("YES")
else:
    print("NO")