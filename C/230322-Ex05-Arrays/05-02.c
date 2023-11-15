#include <stdio.h>

void main(){

    int array[10];
    int operator;

    printf("Geben Sie eine Zahl ein.");
    scanf("%d",&array[0]);getchar();

    printf("Mit 2 oder 3 multiplizieren");
    scanf("%d",&operator);getchar();

    if(operator==2){
        for(int i=1;i<10;i++){
            array[i] = array[i-1] * 2;
        }
    }
    if(operator==3){
        for(int i=1;i<10;i++){
            array[i] = array[i-1] * 3;
        }
    }
    for(int i=0;i<10;i++){
        printf("%d\n", array[i]);
    }
}