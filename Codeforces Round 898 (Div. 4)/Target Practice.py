def Target_grade(target):
    col1,col2=0,0
    sum_target=0
    for row in range(5):
        count=0
        for col in range(col1,10-col1):
            if target[row][col]=="X":
                count+=1
        for i in range(row+1,5):
            if target[i][col1]=="X":
                count+=1
            if target[i][10-col1-1]=="X":
                count+=1
        sum_target+=(count*(row+1))
        col1+=1
    row_temp=0
    for row in range(9,4,-1):
        count=0
        for col in range(col2,10-col2):
            if target[row][col]=="X":
                count+=1
        for i in range(row-1,4,-1):
            if target[i][col2]=="X":
                count+=1
            if target[i][10-col2-1]=="X":
                count+=1
        sum_target+=(count*(row_temp+1))
        row_temp+=1
        col2+=1
    return sum_target

if __name__=="__main__":
    test=int(input())
    while test!=0:
        target=[]
        for _ in range(10):
            row=[]
            string=input()
            for char in string:
                row.append(char)
            target.append(row)
        print(Target_grade(target))
        test-=1