#include <stdio.h>

void main()
{
    float a=5.3;
    float b=4.8;
    float c=10.5;
    float volume;
    float surface;

    volume = a*b*c;
    surface = 2*a*b+2*b*c+2*a*c;
    
    printf("Volumen =%lf\n",volume);
    printf("Fläche = %lf",surface);
}