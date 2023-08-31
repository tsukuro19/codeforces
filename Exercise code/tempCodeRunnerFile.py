    while True:
        if cubes-sum_cubes>0:
            cubes-=sum_cubes
            count+=1
        else:
            break
        sum_cubes+=count
    print(count)