n=int(input())
soliders=list(map(int,input().split()))
min_solider,max_solider=1000,0
min_index,max_index=0,0
for i in range(len(soliders)):
    if soliders[i]>max_solider:
        max_solider=soliders[i]
        max_index=i
    if soliders[i]<=min_solider:
        min_solider=soliders[i]
        min_index=i

if max_index>min_index:
    print((max_index-1)+(n-min_index)-1)
else:
    print((max_index-1)+(n-min_index))