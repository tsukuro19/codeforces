if __name__=="__main__":
    test=int(input())
    while test!=0:
        number=int(input())
        w1,e1=map(int,input().split())
        w_res=w1
        for _ in range(number-1):
            w,e=map(int,input().split())
            if w>=w_res and e>=e1:
                w_res=-1
        print(w_res)
        test-=1