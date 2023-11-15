#include <stdio.h>

void main(){

    int smiley;

    printf("Welchen smiley wollen Sie?");
    scanf("%d",&smiley);getchar();

    if(smiley==1){
        printf(":-)");
    }
    else if(smiley==2){
        printf(":-|");
    }
    else if(smiley==3){
        printf(":-(");
    }
    else{
        printf("Unbekannter Smiley");
    }

}