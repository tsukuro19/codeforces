s=input()
temp=''
vowels=['A','O','Y','E','U','I']
for i in range(len(s)):
    if s[i].upper() not in vowels:
        temp+=s[i]
result='.'.join(temp.lower())
print(''.join(('.',result)))