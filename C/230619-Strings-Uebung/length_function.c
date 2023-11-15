#include <stdio.h>
int main(){
    char text[] ="Mein Beispielstring";
    int i;
    int length=0;
    for (i=0; text[i] !='\0'; i++) {
        length++;  
    }
    printf("Laenge: %d\n", length);
    return 0;
    }