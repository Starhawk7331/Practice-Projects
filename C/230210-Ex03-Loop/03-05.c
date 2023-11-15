#include <stdio.h>

void main(){

    int a,b,sum=0,i;

    printf("Was ist a:");
    scanf("%d",&a);getchar();

    printf("Was ist b:");
    scanf("%d",&b);getchar();

    for (i = a; i <=  b; i++){
        sum +=i;
    }
    printf("%d",sum);
}