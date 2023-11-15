#include <stdio.h>

void main()
{

double cels,Faehr,Kelv;


printf("Was ist die Temperatur in Celsius?\n");

scanf("%lf",&cels);

Faehr = ((cels*9)/5)+32;
Kelv = cels + 273.15;

printf("Kelvin: %lf\n",Kelv);
printf("Faehrenheit: %lf\n",Faehr);


}