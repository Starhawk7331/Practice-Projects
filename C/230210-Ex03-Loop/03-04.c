#include <stdio.h>

void main(){

    int reals,i;
    double sum,holder;

    printf("Wie viele Kommazahlen");
    scanf("%d",&reals);getchar();

    for ( i = 0; i < reals; i++){
        printf("Kommazahl:");
        scanf("%lf",&holder);
        sum+=holder;
    }
    printf("%lf",sum);
}