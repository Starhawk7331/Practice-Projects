#include <stdio.h>

//prototype
#define ARR_SIZE 10

void BubbleSort(int Array[],int size);

void main(){

    int Array[ARR_SIZE] = {34,76,-12,3,0,34,-23,-76,89,16};

    int arr[5] = { 5, 8, 2, 9, 2};

    BubbleSort(Array,ARR_SIZE);
    BubbleSort(arr,ARR_SIZE);
    
    getchar();
}

void BubbleSort(int Array[],int size){

    int swapped;//boolean true....not 0/false...0

    for(int i = 0;i<size-1;i++){
        swapped = 0;
        for(int j = 0;j<size-1-i;j++){
            if(Array[j]>Array[j+1]){
                int temp = Array[j+1];
                Array[j+1] = Array[j];
                Array[j] = temp;
                swapped=1;
            }

        }
        if(!swapped){
            break;
        }

    }

}