#include <stdio.h>

#define ARR_SIZE 10

void InsertionSort(int Array[],int size);

void main(){

    int Array[ARR_SIZE] = {34,76,-12,3,0,34,-23,-76,89,16};
    int rev[6] = { 100,99,98,50,25,10};
    int sim[5] = {3,4,3,4,3};

    InsertionSort(rev,6);
    
    getchar();
}

void InsertionSort(int Array[],int size){

    int temp;

    for(int i = 1;i < size;i++){

        temp = Array[i];

        for(int j = i-1; j >= 0; j--){
            if(temp < Array[j]){
                Array[j+1] = Array[j];
                Array[j] = temp;
            }
            
        }

    }

    for(int i = 0;i<size;i++){
        printf("%d\n",Array[i]);
    }
    
}