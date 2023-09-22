def eraser(paper, k):
    res=0
    index=0
    while index<len(paper):
        if paper[index]=="B":
            res+=1
            index+=k
        else:
            index+=1
    return res



if __name__=="__main__":
    test=int(input())
    while test!=0:
        number,k=map(int,input().split())
        paper=input()
        print(eraser(paper,k))
        test-=1