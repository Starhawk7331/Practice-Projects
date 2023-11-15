#include <stdio.h>

#define ARR_SIZE 5

void main(){


    int Array1[ARR_SIZE] = {2,6,12,7,9};
    int Array2[ARR_SIZE] = {6,4,8,9,0};
    int dups[ARR_SIZE] = {0,0,0,0,0};

    printf("Array1: ");
    for(int i = 0;i<ARR_SIZE;i++){
        printf(" %d", Array1[i]);
    }

    printf("\nArray2: ");
    for(int i = 0;i<ARR_SIZE;i++){
        printf(" %d", Array2[i]);
    }

    for(int i = 0;i<ARR_SIZE;i++){
        for(int j = 0;j < ARR_SIZE;j++){
            if(Array1[i] == Array2[j]){
                dups[i] = Array1[i];
            }
        }
    }
 
    for(int i = 0;i<ARR_SIZE;i++){
        if(dups[i] != 0){
            printf("\n%d kommt in beiden Arrays vor", dups[i]);
        }   
    }
}