n=int(input())
s=input()
s_lower=s.lower()
alphabet='abcdefghijklmnopqrstuvwxyz'
if n<26:
    print("NO")
else:
    count=0
    for i in range(len(alphabet)):
        if alphabet[i] in s_lower:
            count+=1
    if count==26:
        print("YES")
    else:
        print("NO")