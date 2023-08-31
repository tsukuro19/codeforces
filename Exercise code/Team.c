#include<stdio.h>

int main(void){
    int n;
    int temp=0;
    scanf("%d",&n);
    int a[n][3];
    for(int i=0;i<n;i++){
        for(int j=0;j<3;j++){
            scanf("%d",&a[i][j]);
        }
    }
    for(int i=0;i<n;i++){
        int count=0;
        for(int j=0;j<3;j++){
            if(a[i][j]==1)
                count++;
        }
        if(count>=2)
            temp++;
    }
    printf("%d",temp);
    return 0;
}