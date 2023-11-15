#include <stdio.h>

void main()
{
    int radius;
    float circum;

    printf("Was ist der Radius?");
    scanf("%d",&radius);

    circum=2*radius*3.14;

    printf("Der Umfang ist: %lf",circum);

}