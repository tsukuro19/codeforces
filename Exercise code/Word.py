s=input()
up,low=0,0
for i in range(len(s)):
    if s[i].upper()==s[i]:
        up+=1
    else:
        low+=1
if up>low:
    print(s.upper())
elif up<low:
    print(s.lower())
else:
    print(s.lower())