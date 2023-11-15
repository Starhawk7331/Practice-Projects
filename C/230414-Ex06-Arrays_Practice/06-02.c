#include <stdio.h>

#define ARR_SIZE 10

void main(){


    int Array[ARR_SIZE];
    int copy[ARR_SIZE];

    for(int i = 0;i<ARR_SIZE;i++){
        scanf("%d",&Array[i]);getchar();
        copy[i] = Array[i];
    }
   
    for(int i = 0;i<ARR_SIZE;i++){
        printf("%d\n", copy[i]);
    }

}