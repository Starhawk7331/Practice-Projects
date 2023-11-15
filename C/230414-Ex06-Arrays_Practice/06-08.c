#include <stdio.h>

#define ARR_SIZE 30

void print_weather(int array[],int size);
void edit_weather(int array[],int index);

void main(){

    int month[ARR_SIZE];
    int temp;
    char answer,j = 'j';

    for(int i = 0;i < ARR_SIZE; i++){
        edit_weather(month,i);
    }

    print_weather(month,ARR_SIZE);

    do{
        printf("\nMöchten Sie etwas ändern?(j/n): ");
        scanf("%c",&answer);getchar();

        if(answer == 'j'){
            do{

                printf("Welche Stelle?: ");
                scanf("%d",&temp);getchar();

            }while(temp < 0 || temp > ARR_SIZE-1);

            edit_weather(month,temp);
        }

    }while(answer!= 'n');

}
void print_weather(int array[],int size){

    printf("\n\nWetteraufzeichnung\n==================\n");

    for(int i = 0;i < size;i++){
        printf("Wetter von Tag %d: ", i+1);
        
        if(array[i] == 1){
            printf("Sonnenschein\n");
        }
        else if(array[i] == 2){
            printf("Wolken\n");
        }
        else if(array[i] == 3){
            printf("Regen\n");
        }
        else if(array[i] == 4){
            printf("Schnee\n");
        }
        else{
            printf("Keine Info\n");
        }
    }
}
void edit_weather(int array[],int index){

    do{

        printf("Wetter von Tag %d: ", index+1);
        scanf("%d",&array[index]);getchar();

    }while(array[index] < 0 || array[index] > 4);

}