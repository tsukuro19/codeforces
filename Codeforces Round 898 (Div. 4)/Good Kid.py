def Good_kid(present):
    product=1
    present[present.index(min(present))]+=1
    for i in range(len(present)):
        product*=present[i]
    return product


if __name__=="__main__":
    test=int(input())
    while test!=0:
        number=int(input())
        present=list(map(int,input().split()))
        print(Good_kid(present))
        test-=1