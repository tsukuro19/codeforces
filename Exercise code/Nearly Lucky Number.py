n=int(input())
n_str=str(n)
count=0
for i in range(len(n_str)):
    if n_str[i]=='4' or n_str[i]=='7':
        count+=1
if count==4 or count==7:
    print("YES")
else:
    print("NO")
