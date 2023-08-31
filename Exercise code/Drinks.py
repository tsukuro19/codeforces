n=int(input())
cocktails=list(map(int,(input().split())))
for i in range(len(cocktails)):
    cocktails[i]=cocktails[i]/100
result=(sum(cocktails)/n)*100
print('{:.12f}'.format(round(result,12)))