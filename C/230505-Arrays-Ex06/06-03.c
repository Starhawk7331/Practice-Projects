#include <stdio.h>

void main(){

    int array[5] = { 13, 5, 1, 27, 3 };
    int swapped = 0, temp;


    do{
        swapped = 0;

        for(int i = 0;i < 4;i++){

            if(array[i] > array[i+1]){
                temp = array[i];
                array[i] = array[i+1];
                array[i+1] = temp;

                swapped += 1;
            }
            
        }

    }while(swapped != 0);


    for(int i = 0;i < 5;i++){
        printf("%d\n",array[i]);
    }
}