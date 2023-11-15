#include <stdio.h>

void main(){

    char first_name[30];
    char last_name[30];
    char full_name[61];

    printf("First name:");
    fgets(first_name,30,stdin);

    printf("Last name:");
    fgets(last_name,30,stdin);

    for(int i = 0;first_name[i] != '\0';i++){
        if(first_name[i] == '\n'){
            first_name[i] = '\0';
        }
        else{
            first_name[i] = toupper(first_name[i]);
        }
    }

    for(int i = 0;last_name[i] != '\0';i++){
        if(last_name[i] == '\n'){
            last_name[i] = '\0';
        }
        else{
            last_name[i] = tolower(last_name[i]);
        }
    }
    int i = 0;

    for(i = 0;first_name[i] != '\0';i++){
        full_name[i] = first_name[i];
    }
    full_name[i] = '_';
    i++;

    for(int n = 0;last_name[n] != '\0';n++){
        full_name[i] = last_name[n];
        i++;
    }
    i++;
    full_name[i] == '\0';

    printf("%s",full_name);

}