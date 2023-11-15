#include <stdio.h>

void main(){
    int z;

    do{
        printf("Enter number between 0 and 36");
        scanf("%d",&z);getchar();

    }while (z < 0 || z > 36);

    if(z == 0){
        printf("zero");
    }
    else if(z%2 == 0){
        printf("even");
    }
    else{
        printf("odd");
    }
}