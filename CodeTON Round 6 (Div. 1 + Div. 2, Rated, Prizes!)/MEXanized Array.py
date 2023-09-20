def find_mex(arr, n):
    seen = [False] * (n + 1)

    for num in arr:
        if num < n + 1:
            seen[num] = True

    for i in range(n + 1):
        if not seen[i]:
            return i

    return n + 1


def mexanized_arrayy(number,mex,limit):
    result=[]
    for num in range(0,number):
        if num>=mex or num>=limit:
            if limit==mex :
                result.append(limit-1)
            else:
                result.append(limit)
        else:
            result.append(num)
    if find_mex(result,number)==mex:
        return sum(result)
    else:
        return -1

if __name__=="__main__":
    test=int(input())
    while test!=0:
        number,mex,limit=map(int,input().split())
        print(mexanized_arrayy(number,mex,limit))
        test-=1