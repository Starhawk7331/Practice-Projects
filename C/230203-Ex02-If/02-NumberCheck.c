#include <stdio.h>

void main()
{

double num;

printf("Geben Sie eine Zahl ein.");
scanf("%lf",&num);getchar();

if(num<0){
    printf("Kleiner als 0");
}else if(num==0){
    printf("Gleich 0");
}else{
    printf("Größer als 0");
}


}