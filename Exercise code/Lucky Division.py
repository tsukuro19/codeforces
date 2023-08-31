n=int(input())
check=0
a=[4,7,47,74,44,77,444,777,447,477,774,747,744]
for i in range(len(a)):
    if n%a[i]==0:
       check+=1
       break
if check==1:
    print("YES") 
else:
    print("NO")
