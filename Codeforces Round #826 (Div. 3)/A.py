def Solution(s1,s2):
    if s1[len(s1)-1]==s2[len(s2)-1]:
        if s1[len(s1)-1]=='L':
            if s1.count('X')>s2.count('X'):
                print('>')
            elif s1.count('X')<s2.count('X'):
                print('<')
            else:
                print('=')
        else:
            if s1.count('X')>s2.count('X'):
                print('<')
            elif s1.count('X')<s2.count('X'):
                print('>')
            else:
                print('=')
    else:
        if s1[len(s1)-1]=='L':
            print('>')
        elif s1[len(s1)-1]=='S':
            print('<')
        else:
            if s2[len(s2)-1]=='M':
                print('=')
            elif s2[len(s2)-1]=='S':
                print('>')
            else:
                print('<')

t=int(input())
while t!=0:
    s1,s2=map(str,input().split(' '))
    Solution(s1,s2)
    t-=1