#include<stdio.h>
#include<stdlib.h>

int main(void){
    int n,*p,i,j;
    scanf("%d",&n);
    p=(int*)calloc(n,sizeof(int));
    for(i=0;i<n;i++){
        scanf("%d",(p+i));
    }
    for(i=0;i<n;i++){
        int temp=0;
        for(j=*(p+i);;j++){
            if(((*(p+i) & *(p+j))>0) && ((*(p+i) | *(p+j))>0)){
                temp=j;
                break;
            }
        }
        printf("%d\n",temp);
    }
    free(p);
    return 0;
}