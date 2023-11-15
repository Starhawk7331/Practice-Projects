#include <stdio.h>

void main(){

    int num;

    do
    {
        printf("Zahll zwischen 1-5\n");
        scanf("%d",&num);
    } while (num<=0||num>5);
    
}