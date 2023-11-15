#include <stdio.h>

int search(int arr1[],int size1,int arr2[],int size2);

void main(){

    int values3[5] = {-1,0,1,2,3};
    int searchVals[3] = {1,1,1};

    printf("Example3: %d",search(values3,5,searchVals,3));
}

int search(int arr1[],int size1,int arr2[],int size2){

    int count = 0;

    for(int i = 0;i < size1;i++){
        for(int n = 0;n < size2;n++){
            if(arr1[i] == arr2[n]){
                count += 1;
                break;
            }
        }
    }
    return count;
}
