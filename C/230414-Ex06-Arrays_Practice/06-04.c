#include <stdio.h>

#define ARR_SIZE 5

void main(){


    double Array[ARR_SIZE] = {3.4,5.6,2.1,7.9,4.8};
    double min = Array[0],max = Array[0];

    for(int i = 1;i<ARR_SIZE;i++){
        if(Array[i] < min){
            min = Array[i];
        }
        if(Array[i] > max){
            max = Array[i];
        }
        
    }
   
    printf("max: %lf\nmin: %lf",max,min);

}