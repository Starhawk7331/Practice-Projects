#include <stdio.h>

#define ARR_SIZE 5

void main(){


    int Array[ARR_SIZE] = {3,17,29,38,45};
    int sum = 0;
    double average;


    for(int i = 0;i<ARR_SIZE;i++){
        sum += Array[i];
    }
    average = sum / ARR_SIZE;

    printf("Die Zahlen sind:");
   
    for(int i = 0;i<ARR_SIZE;i++){
        printf(" %d ", Array[i]);
    }

    printf("\nDie Summe ist: %d\n",sum);
    printf("Der Mittelwert ist: %lf\n",average);

    for(int i = 0;i<ARR_SIZE;i++){
        if(Array[i]<average){
            printf("%d liegt unter dem Mittelwert\n", Array[i]);
        }
        else{
            printf("%d liegt ueber dem Mittelwert\n",Array[i]);
        }

    }
}