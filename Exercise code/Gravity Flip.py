#https://www.entechin.com/how-to-print-a-list-without-square-brackets-in-python/
n=int(input())
a=list(map(int,input().strip().split()))
print(' '.join(map(str,sorted(a))))