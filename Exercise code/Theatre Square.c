#include<stdio.h>

int main(void){
    long long int n,m,a;
    scanf("%lld %lld %lld",&n,&m,&a);
    long long int sum=((n+a-1)/a)*((m+a-1)/a);
    printf("%lld",sum);
    return 0;
}