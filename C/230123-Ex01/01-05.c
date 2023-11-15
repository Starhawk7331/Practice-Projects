#include <stdio.h>

void main()
{
double weight,height,BMI;

printf("Geben Sie ihre größe in Meter an.\n");

scanf("%lf",&height);

printf("Geben Sie ihr Gewicht in Kilogramm an.\n");

scanf("%lf",&weight);

BMI = weight/(height*height);

printf("Ihr BMI ist: %lf",BMI);

}