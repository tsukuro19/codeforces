shoes=list(map(int,input().split()))
dict_shoes={}
count=0
for i in range(len(shoes)):
    if shoes.count(shoes[i])>1:
        dict_shoes[shoes[i]]=shoes.count(shoes[i])
for value in dict_shoes.values():
    count+=value-1
print(count)