def compare(bList,gList):
    result=0
    for i in range(len(bList)):
        for j in range(len(gList)):
            if abs(bList[i]-gList[j])<=1:
                result+=1
                gList[j]=1000
                break
    return result


b=int(input())
b_list=list(map(int,input().split()))
g=int(input())
g_list=list(map(int,input().split()))
b_list=sorted(b_list)
g_list=sorted(g_list)
print(compare(b_list,g_list))