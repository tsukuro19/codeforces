cubes=int(input())
height,count=0,0
while cubes>height+count:
    height+=1
    count+=height
    cubes-=count
print(height)