s=input()
if s[0]==s[0].upper():
    print(s)
else:
    temp=list(s)
    temp[0]=s[0].upper()
    s="".join(temp)
    print(s)