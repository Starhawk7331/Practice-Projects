#include <stdio.h>

#define ARR_SIZE 5

void get_grade(int average);

void main(){

    int grade[ARR_SIZE];
    int sum = 0,participation;
    double average;


    for(int i = 0;i<ARR_SIZE;i++){

        do{
            printf("Note %d. Schularbeit: ", i+1);
            scanf("%d",&grade[i]);getchar();

        }while(grade[i] < 1 || grade[i] >5);
        sum += grade[i];
    }
    

    do{
        printf("Was ist die Mitarbeitsnote?0 wenn es keine gibt\n");
        scanf("%d",&participation);
    }while(participation < 0 ||participation > 5);

    if(participation != 0){
        average = (double)(sum + participation) / (ARR_SIZE + 1);
    }
    else{
        average = (double)sum / ARR_SIZE;
    }

    printf("Notendurchschnitt: %.2lf\n", average);
    get_grade(average);
   
}

void get_grade(int average){
    if(average < 2){
        printf("Sehr Gut");
    }
    else if(average < 3){
        printf("Gut");
    }
    else if(average < 4){
        printf("Befriedigend");
    }
    else if(average < 5){
        printf("Genügend");
    }
    else if(average == 5){
        printf("Nicht Genügend");
    }
}
