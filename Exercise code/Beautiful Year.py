n=int(input())
while True:
    n+=1
    list_n=[int(x) for x in str(n)]
    dup={x for x in list_n if list_n.count(x)>1}
    if len(dup)>0:
        continue
    else:
        break
print(n)