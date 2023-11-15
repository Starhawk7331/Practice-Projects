#include <stdio.h>

void main(){

    int points;

    printf("Punkte:");
    scanf("%d",&points);getchar();

    if(points>24){
        printf("Ungueltig");
    }
    else if(points<0){
        printf("Ungueltig");
    }
    else if(points<13){
        printf("Nicht Genuegend");
    }
    else if(points<16){
        printf("Genuegend");
    }
    else if(points<20){
        printf("Befriedigend");
    }
     else if(points<22){
        printf("Gut");
    }
     else if(points<25){
        printf("Sehr Gut");
    }
    





}