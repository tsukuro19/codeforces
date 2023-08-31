n=int(input())

matrix=[]
for i in range(n):
    a=[]
    for j in range(3):
        a.append(int(input()))
    matrix.append(a)

#Solution
temp=0
for i in range(n):
    count=0
    for j in range(3):
        if(matrix[i][j]==1):
            count+=1
    if(count>=2):
        temp+=1
print(temp)