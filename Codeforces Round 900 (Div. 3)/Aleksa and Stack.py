def array_number(number):
    res=[6,8,12]
    for i in range(2,number):
        element=res[i]+1
        while (element*3)%(res[i]+res[i-1])==0:
            element+=1
        res.append(element)
    return res
 
if __name__=="__main__":
    test=int(input())
    while test!=0:
        number=int(input())
        result=array_number(number)
        for i in range(number):
            print(result[i],end=" ")
        print()
        test-=1