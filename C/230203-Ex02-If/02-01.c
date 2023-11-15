#include <stdio.h>

void main(){

    int number;

    printf("Please enter a number\n");
    scanf("%d",&number);getchar();
    
    if(number%2==0){
        printf("Die Zahl ist gerade\n");
    }else{
        printf("Die Zahl ist ungerade\n");
    }
    if(number<=10){
        printf("Kleiner gleich 10\n");
    }else if(number>20){
        printf("Groesser als 20\n");
    }else if(number!=0){
        printf("nicht gleich 0\n");
    }
}