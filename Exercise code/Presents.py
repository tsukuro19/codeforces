n=int(input())
present=list(map(int,input().split()))
dict_present={}
for i in range(1,len(present)+1):
    dict_present[present[i-1]]=i
result=[]
for i in range(1,len(dict_present)+1):
    result.append(dict_present[i])
print(*result,sep=' ')