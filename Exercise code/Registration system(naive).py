def registration_system(a):
    system=[]
    duplicate=[]
    for i in range(len(a)):
        if a[i] not in system:
            print("OK")
            system.append(a[i])
        else:
            duplicate.append(a[i])
            print(a[i]+str(duplicate.count(a[i])))


n=int(input())
a=[]
for i in range(n):
    i=input()
    a.append(i)
registration_system(a)