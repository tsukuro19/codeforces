n=int(input())
result='I hate it'
result_temp='I hate that'
if n==1:
    print(result)
elif n==2:
    print(result_temp+" "+"I love it")
else:
    i=2
    while i<=n-1:
        if i%2==0:
            result_temp=result_temp+" "+"I love that"
        else:
            result_temp=result_temp+" "+"I hate that"
        i+=1
    if n%2==0:
        print(result_temp+" "+"I love it")
    else:
        print(result_temp+" "+"I hate it")