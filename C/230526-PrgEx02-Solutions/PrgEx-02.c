#include <stdio.h>
#include <math.h>

double getHypothenuse(int a, int b);

void main(){

    double a = 4;
    double b = 3;

    double c = getHypothenuse(a,b);

    if(c == 5){
        printf("Korrekt");
    }
    else{
        printf("Incorrect");
    }
}

double getHypothenuse(int a, int b){
    double hypo = sqrt(a*a+b*b);
    return hypo;
}
