#include <stdio.h>

void main()
{


    char firstname;
    char surname;

    printf("Bitte erster Buchstabe des vornamens eingeben:\n");
    firstname=getchar(); getchar();

    printf("Bitte erster Buchstabe des Nachnamens eingeben:\n");
    surname=getchar(); getchar();
    
    printf("Dein Namenskuerzel ist %c%c",firstname,surname);


}