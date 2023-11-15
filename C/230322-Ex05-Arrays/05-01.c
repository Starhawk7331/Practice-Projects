#include <stdio.h>

void main(){

    char letters[5];

    for(int i=0;i<5;i++){
        printf("Geben Sie einen Buchstaben ein.");
        scanf("%c",&letters[i]);getchar();
    }
    
    for(int i=0;i<5;i++){
        printf("%c",letters[i]);
    }
    
    
}
