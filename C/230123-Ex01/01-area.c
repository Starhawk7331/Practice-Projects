#include <stdio.h>

void main()
{
    int radius;
    float area;

    printf("Geben Sie den Radius ein:\n");
    scanf("%d",&radius);

    area=radius*radius*3.14;

    printf("%lf",area);
}