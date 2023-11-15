#include <stdio.h>

void compare(char arr1[],char arr1Size,char arr2[],char Arr2Size,char results[]);

void main(){

    char arr1a[]= {'a','b','c'};
    char arr2a[]= {'b','c','a'};

    char arr1b[]= {'x','y','z','3'};
    char arr2b[]= {'x','x','3'};

    char arr1c[]= {'x','a'};
    char arr2c[]= {'b','c','d'};

    char result[5];

    compare(arr1a,3,arr2a,3,result);

    for(int i = 0;i < 5;i++){
        if(result[i] == '\0'){
            break;
        }
        printf("%c\n",result[i]);
    }
    
}


void compare(char arr1[],char arr1Size,char arr2[],char Arr2Size,char results[]){

    int pos = 0;

    for(int i = 0;i < arr1Size;i++){
        for(int n = 0;n < Arr2Size;n++){
            if(arr1[i] == arr2[n]){
                results[pos] = arr1[i];
                pos++;
                break;
            }
        }
    }
    results[pos] = '\0';

}