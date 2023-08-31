def Insertion_sort(tower,n):
    for i in range(len(tower)):
        key=tower[i]
        j=i-1
        while j>-1 and tower[j]>key:
            tower[j+1]=tower[j]
            j-=1
        tower[j+1]=key
    return tower 


def Count_tower(tower,n):
    tower_sorted=Insertion_sort(tower,n)
    set_tower,count=[],1
    for i in range(n):
        if tower_sorted[i] in set_tower:
            continue
        set_tower.append(tower_sorted[i])
    for i in range(len(set_tower)):
        temp=0
        for j in range(len(tower_sorted)):
            if set_tower[i]==tower_sorted[j]:
                temp+=1
        if temp>count:
            count=temp
    return "{0} {1}".format(count,len(set_tower))


if __name__=="__main__":
    n=int(input())
    tower=list(map(int,input().split()))
    print(Count_tower(tower,n))