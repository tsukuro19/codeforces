def check_daytona(numbers,n,k):
    if numbers.count(k)==0:
        return "NO"
    return "YES"


if __name__=="__main__":
    test=int(input())
    while test!=0:
        n,k=map(int,input().split())
        numbers=list(map(int,input().split()))
        print(check_daytona(numbers,n,k))
        test-=1