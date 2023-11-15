#include <stdio.h>
#include <string.h>

void main(){

    char origin[] = "A text copy";
    char copy[50] ={'a','b','c','\0'};

    if(strncmp(origin,copy,50) == 0){
        printf("Equal");
    }
    else{
        printf("not equal");
    }
    printf("before: %s\n", copy);

    strncpy(copy,origin,50);

    printf("Copy: %s", copy);

    if(strncmp(origin,copy,50) == 0){
        printf("Equal");
    }
    else{
        printf("not equal");
    }

}