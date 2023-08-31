n,t=map(int,input().split())
s=input()
x=0
list_s=[x for x in s]
while x<t:
    i=0
    while i<n-1:
        if list_s[i]=='B' and list_s[i+1]=='G':
            list_s[i],list_s[i+1]=list_s[i+1],list_s[i]
            i+=2
        else:
            i+=1
    x+=1
print(''.join(list_s))