n=int(input())
stop_tram=[]
dict_total={}
for i in range(n):
    stop_tram.append(list(map(int,input().split())))
    if i==0:
        dict_total[i]=stop_tram[0][1]
    else:
        dict_total[i]=dict_total[i-1]-stop_tram[i][0]+stop_tram[i][1]
print(max(dict_total.values()))