#include <stdio.h>

void main(){

    double weight,height,BMI;

    printf("Geben Sie ihre größe in Meter an.\n");

    scanf("%lf",&height);

    printf("Geben Sie ihr Gewicht in Kilogramm an.\n");

    scanf("%lf",&weight);

    BMI = weight/(height*height);

    printf("Ihr BMI ist: %lf\n",BMI);

    if(BMI<20){
        printf("Untergewicht");
    }
    else if(BMI<25){
        printf("Normalgewicht");
    }
    else if(BMI<30){
        printf("Übergewicht");
    }
    else{
        printf("Starkes Übergewicht");
    }


}