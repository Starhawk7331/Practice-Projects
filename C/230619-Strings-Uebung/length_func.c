#include <stdio.h>

int str_len(char str[]);

void main(){

    char str[] = {"Srvus geiseln"};

    int length = str_len(str);

    printf("%d",length);
}

int str_len(char str[]){

    int len = 0;

    while(str[len] != '\0'){
        len++;
    };

    return len;


}