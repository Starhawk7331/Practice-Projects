#include <stdio.h>

#define ARR_SIZE 6

void main(){

    int Array[ARR_SIZE] = {4,8,15,16,23,42};
    int temp;

    Array[5] = 99;

    temp = Array[2];
    Array[2] = Array[3];
    Array[3] = temp;

    for(int i = 0;i<ARR_SIZE;i++){
        printf("%d\n", Array[i]);
    }

}