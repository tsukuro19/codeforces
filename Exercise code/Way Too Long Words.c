#include<stdio.h>
#include<string.h>

int main(void){
    char c[1000];
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        scanf("%s",c);
        int temp=strlen(c);
        if(strlen(c)<=10)
            printf("%s\n",c);
        else
            printf("%c%d%c\n",c[0],strlen(c)-2,c[temp-1]);
    }
    return 0;
}