def Two_vessels(bottle_a,bottle_b,c):
    if bottle_a==bottle_b:
        return 0
    else:
        diff=abs(bottle_a-bottle_b)/2
        if diff==int(diff):
            if diff%c==0:
                return int(diff//c)
            else:
                return int((diff//c)+1)
        else:
            int_diff=diff//c
            if int_diff%c==0:
                return int((diff//c)+1)
            else:
                return int((diff//c)+1)

if __name__=="__main__":
    test=int(input())
    while test!=0:
        bottle_a,bottle_b,c=map(int,input().split())
        print(Two_vessels(bottle_a,bottle_b,c))
        test-=1