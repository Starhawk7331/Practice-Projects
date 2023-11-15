#include <stdio.h>

void main();
double powerof();

void main(){
    int a = 2,b = -3;
    printf("%lf",powerof(a,b));
}

double powerof(a,b){
    double result = 1;
    int x;

    if(b<0){
        x = b * -1;
    }

    for(int i = 1;i <= x;i++){
        result = result * a;
    }

    if(b<0){
        result = 1/result;
    }
        
    return result;
}