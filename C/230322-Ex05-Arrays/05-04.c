#include <stdio.h>

#define SIZE 5

void main();
void BarGraph(int arr[],int size);

void main(){
    int stars[SIZE];
    stars[0]=2;
    stars[1]=1;
    stars[2]=2;
    stars[3]=2;
    stars[4]=6;

    BarGraph(stars,SIZE);

}

void BarGraph(int arr[],int size){

    for(int i=0;i<SIZE;i++){
        for(int n=0;n<arr[i];n++){
            printf("*");
        }
        printf("\n");
    }
}