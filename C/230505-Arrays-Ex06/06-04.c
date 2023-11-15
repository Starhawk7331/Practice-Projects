#include <stdio.h>

void SelectionSort(int array[],int arr_size);
void InsertionSort(int array[],int arr_size);

void main(){


    int array[] = { 13, 5, 1, 27, 3 };

   
    InsertionSort(array,5);

}

void SelectionSort(int array[],int arr_size){

    int minimum,temp;

    for(int i = 0;i < arr_size; i++){

        minimum = i;

        for(int n = i+1;n < arr_size;n++){
            if(array[n] < array[minimum]){
                minimum = n;
            }
        }

        temp = array[i];
        array[i] = array[minimum];
        array[minimum] = temp;

    }

    for(int i = 0;i<arr_size;i++){
        printf("%d\n",array[i]);
    }

}

void InsertionSort(int array[],int arr_size){

    int temp;

    for(int i = 1;i < arr_size;i++){

        temp = array[i];

        for(int n = i - 1;n >= 0;n--){

            if(temp < array[n]){

                array[n+1] = array[n];
                array[n] = temp;
                
            }
        }
    }
    
    for(int i = 0;i<arr_size;i++){
        printf("%d\n",array[i]);
    }
}