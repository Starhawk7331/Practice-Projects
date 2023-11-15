#include <stdio.h>

#define ARR_SIZE 10

void SelectionSort(int Array[],int size);

void main(){

    int Array[ARR_SIZE] = {34,76,-12,3,0,34,-23,-76,89,16};
    int rev[6] = { 100,99,98,50,25,10};
    int sim[5] = {3,4,3,4,3};

    SelectionSort(Array,ARR_SIZE);
    
    getchar();
}

void SelectionSort(int Array[],int size){

    int Minimum,temp;

    for(int i = 0;i<size;i++){

        Minimum = i;
        
        for(int j = i+1;j<size;j++){
            if(Array[j] < Array[Minimum]){
                Minimum = j;  
            }
            
        }
        temp = Array[Minimum];
        Array[Minimum] = Array[i];
        Array[i] = temp;
        
    }
    for(int i = 0;i<size;i++){
        printf("%d\n",Array[i]);
    }
    
}