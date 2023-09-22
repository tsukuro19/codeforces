def solve():
    column,water=map(int,input().split())
    columns=list(map(int,input().split()))
    left,hi=0,2e9
    while(left<hi):
        mid=left+(hi-left+1)//2
        result=0
        for i in range(column):
            result+=max(mid-columns[i],0)
        if (result<=water):
            left=mid
        else:
            hi=mid-1
    return int(left)


if __name__=="__main__":
    test=int(input())
    while test!=0:
        print(solve())
        test-=1