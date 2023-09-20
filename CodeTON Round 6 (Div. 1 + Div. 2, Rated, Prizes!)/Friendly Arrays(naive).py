def xor_array(array):
    x=array_1[0]
    for i in range(1,len(array_1)):
        x^=array_1[i]
    return x
 
 
def Friendly_array(array_1,array_2):
    min_array,max_array=xor_array(array_1),xor_array(array_1)
    for i in range(len(array_2)):
        temp=array_1
        for j in range(len(array_1)):
            temp[j]=array_2[i]|temp[j]
        if xor_array(temp)<min_array:
            min_array=xor_array(temp)
        if xor_array(temp)>max_array:
            max_array=xor_array(temp)
    return "{0} {1}".format(min_array,max_array)
 
 
if __name__=="__main__":
    test=int(input())
    while test!=0:
        number_array_1,number_array_2=map(int,input().split())
        array_1=list(map(int,input().split()))
        array_2=list(map(int,input().split()))
        print(Friendly_array(array_1,array_2))
        test-=1