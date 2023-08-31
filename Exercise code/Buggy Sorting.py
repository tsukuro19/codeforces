if __name__=='__main__':
    n=int(input())
    if n>2:
        for i in range(n,0,-1):
            print(i,end=' ')
    else:
        print(-1)