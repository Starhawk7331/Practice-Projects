#include <stdio.h>
#include <math.h>

void main()
{
    double pi =3.141596;
    double a,b,c;

    printf("Geben Sie a ein\n ");
    scanf("%lf",&a);getchar();
    
    printf("Geben Sie b ein");
    scanf("%lf",&b);getchar();

    c=sqrt(a*a+b*b);
    printf("Hypothenus c=%lf",c);

}