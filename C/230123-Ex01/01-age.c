#include <stdio.h>

void main()
{
    char name;
    int age;

    printf("Geben Sie den ersten Buchstaben ihres Namens ein:\n");
    name=getchar();getchar();

    printf("Wie alt sind Sie?");
    
    scanf("%d",&age);

    printf("Sie sind %d",age);
    printf(" Jahre alt mit dem Namen %c",name);


}