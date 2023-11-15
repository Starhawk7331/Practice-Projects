#include <stdio.h>

void letter_swap(char str[],char search,char rep);

void main(){

    char text[] = {"Hello World"};

    letter_swap(text,'l','X');

    printf("%s",text);
}

void letter_swap(char str[],char search,char rep){

    for(int i = 0;str[i] != '\0';i++){
        if(str[i] == search){
            str[i] = rep;
        }
    }

}