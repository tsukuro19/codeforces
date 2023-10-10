def check_sum(number,k,sum_x):
    sum_number=sum(i for i in range(1,number))
    if sum_x>sum_number:
        return "NO"
    elif sum_x==sum_number:
        if k!=number:
            return "NO"
        else:
            return "YES"
    else:
        


if __name__=="__main__":
    test=int(input())
    while test!=0:
        number,k,sum_x=map(int,input().split())
        print(check_sum(number,k,sum_x))
        test-=1