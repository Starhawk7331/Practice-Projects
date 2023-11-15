#include <stdio.h>

void main()
{

double sum, total,Tip;

printf("Was ist die Summe?\n");

scanf("%lf",&sum);

printf("Wie viel Trinkgeld wollen Sie geben?\n");

scanf("%lf",&Tip);

total = sum * Tip;

printf("Gesamt: %lf",total);

}