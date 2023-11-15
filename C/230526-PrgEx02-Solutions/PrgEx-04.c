#include <stdio.h>

#define SIZE 5

void insertSort(int array[],int size);

void main(){
    int arr[SIZE] = {29,10,14,37,14};
    insertSort(arr,SIZE);
}

void insertSort(int array[],int size){
    for(int j = 1;j < size;j++){
        int key = array[j];
        int i = j-1;
        while((i > -1) &&(array[i] > key)){
            array[i+1] = array[i];
            i--;
        }
        array[i+1] = key;
    }
}
