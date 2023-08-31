n,l=map(int,input().split())
lan=list(map(int,input().split()))
lan=sorted(lan)
cmp=max(lan[0],(l-lan[-1]))
for i in range(n-1):
    cmp=max(cmp,(lan[i+1]-lan[i])/2)
print("%.9f" % cmp)