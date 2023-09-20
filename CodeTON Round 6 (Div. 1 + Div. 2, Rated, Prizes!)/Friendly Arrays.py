def xor_array(array):
    x=array[0]
    for i in range(1,len(array)):
        x^=array[i]
    return x

def or_array(array):
    x=array[0]
    for i in range(1,len(array)):
        x|=array[i]
    return x

def Friendly_array(array_1,array_2):
    min_array=xor_array(array_1)
    or_array_2=or_array(array_2)
    for i in range(len(array_1)):
        array_1[i]=array_1[i]|or_array_2
    if(len(array_1)%2!=0):
        return "{0} {1}".format(min_array,xor_array(array_1))
    else:
        return "{0} {1}".format(xor_array(array_1),min_array)


if __name__=="__main__":
    test=int(input())
    while test!=0:
        number_array_1,number_array_2=map(int,input().split())
        array_1=list(map(int,input().split()))
        array_2=list(map(int,input().split()))
        print(Friendly_array(array_1,array_2))
        test-=1