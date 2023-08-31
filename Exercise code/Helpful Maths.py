def Solution(s):
    list_string=[]
    for i in range(len(s)):
        if s[i]=='+':
            s.replace(s[i],'')
        else:
            list_string.append(s[i])
    new_str=''.join(map(str,sorted(list_string)))
    if len(new_str)==1:
        print(new_str)
    else:
        for i in range(0,len(new_str)):
            if i!=len(new_str)-1:
                print(new_str[i],end='+')
            else:
                print(new_str[i])

s=input()
Solution(s)