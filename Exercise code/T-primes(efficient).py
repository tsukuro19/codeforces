from math import sqrt

'''
    The problem is to find if a number is a T prime.
    A number is called a T prime if it has only 3 divisors.
    Solution:
    =========
    A number is a T prime if it is a perfect square
    and its square root is a prime number.
    4 is the only even number which is a T prime number.
'''


limit = 1000000
def prime_flag():
    prime_flag = [True] * limit
    prime_flag[0] = prime_flag[1] = False
    for i in range(2,limit):
        if prime_flag[i] == True:
            for j in range(i*i, limit, i):
                prime_flag[j] = False
    return prime_flag

def check_t_prime(t):
    if t==4:
        return True
    if t<4 or t%2==0:
        return False
    if sqrt(t)==int(sqrt(t)):
        if prime[int(sqrt(t))]==True:
            return True
    return False

prime=prime_flag()
n=int(input())
t=list(map(int,input().split()))
for i in range(len(t)):
    if check_t_prime(t[i])==True:
        print("YES")
    else:
        print("NO")