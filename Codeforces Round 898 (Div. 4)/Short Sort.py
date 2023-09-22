def Short_sort(string):
    if string==''.join(sorted(string)) or string=="cba":
        return "YES"
    else:
        count=0
        for i in range(2):
            for j in range(i,3):
                if string[i]>string[j]:
                    temp = list(string)
                    temp[i], temp[j] = temp[j], temp[i]
                    count+=1
        if count > 1 :
            return "NO"
        else:
            return "YES"

if __name__=="__main__":
    test=int(input())
    while test!=0:
        string=input()
        print(Short_sort(string))
        test-=1