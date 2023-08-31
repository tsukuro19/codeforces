#https://codeforces.com/blog/entry/6419
def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


def Beautiful_Matrix(matrix):
    ls=index_2d(matrix,1)
    return abs(3-(ls[0]+1))+abs(3-(ls[1]+1))


matrix=[]
for i in range(5):
    single_row=list(map(int,input().split()))
    matrix.append(single_row)
print(Beautiful_Matrix(matrix))