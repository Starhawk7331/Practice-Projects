#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void chartoint(char chars[],int ints[]);

void main(){

    char text[] = {"daniel"};
    int ints[10];

    chartoint(text,ints);
}

void chartoint(char text[],int ints[]){

    for(int i = 0;text[i] != '\0';i++){
        ints[i] = text[i];
    }

}