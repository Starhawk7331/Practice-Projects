#include <stdio.h>

#define ARR_SIZE 3

void print_inventory(int Array[]);

void main(){


    int Array[ARR_SIZE] = {10,10,5};
    int choice;

    printf("Getraenkeautomat.Geben Sie 0 ein um das Programm zu beenden\n");
    
    do{

        print_inventory(Array);

        do{
            printf("Ihre Auswahl:");
            scanf("%d",&choice);getchar();

        }while(choice < 0 || choice > 3);

        if(choice != 0){
            Array[choice-1] -= 1;
            printf("Bitte entnehmen Sie den Fruchtsaft!\n");
        }

    }while(choice != 0);

    printf("Wir danken Sie für Ihren Einkauf!");
   
}

void print_inventory(int Array[]){

    printf("1.Wasser: %d\n",Array[0]);
    printf("2.Fruchtsaft: %d\n",Array[1]);
    printf("3.Eistee: %d\n",Array[2]);

}