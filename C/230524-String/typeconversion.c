#include <stdio.h>
#include <stdlib.h>

void main(){

    char num1[] ="123";
    char num2[] = "3.1415";

    int i = atoi(num1);
    printf("atoi: %d\n", i);

    double d = atof(num2);
    printf("atof: %lf\n", d);

    double sum = i + d;
    printf("Sum: %lf\n",sum);
}