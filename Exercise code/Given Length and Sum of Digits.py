m,s=map(int,input().split())
result1,result2="",""
if s>m*9:
    print(-1,-1)
elif m==1 and s==0:
    print(0,0)
elif s==0 and m!=1:
    print(-1,-1)
else:
    for i in range(m):
        k=min(s,9)
        result1+=str(k)
        s-=k
    for i in range(m-1,-1,-1):
        result2+=result1[i]
    i=0
    while result2[i]=="0":
        i+=1
    result2=result2[:i]+str(int(result2[i])-1)+result2[i+1:]
    result2=result2[:0]+str(int(result2[0])+1)+result2[1:]
    print(result2,result1)
    
    
    

