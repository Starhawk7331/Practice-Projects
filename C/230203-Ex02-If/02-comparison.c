#include <stdio.h>

void main(){

    int a,b;

    a=3;
    b=5;

    if(a==b){
        printf("Gleiche Zahlen");
    }else {
        if(a<b){
            printf("a ist kleiner als b");
        } else if(a>b){
            printf("a ist größer als b");
        }else if(a!=b){
            printf("a ist nicht gleich b");
        }
    }
}