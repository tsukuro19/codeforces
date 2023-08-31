def check_zero(a,b):
    sum_check=a+b
    str_a,str_b,str_sum=str(a),str(b),str(sum_check)
    if (int(str_a.replace("0",""))+int(str_b.replace("0","")))==int(str_sum.replace("0","")):
        print("YES")
    else:
        print("NO")


a=int(input())
b=int(input())
check_zero(a,b)