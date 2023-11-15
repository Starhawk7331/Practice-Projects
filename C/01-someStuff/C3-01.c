# include <stdio.h>

int main()
{

int i;

printf("Geben Sie eine Zahl ein:\n");

scanf("%d", &i); getchar();

if(i>0){
    printf("Die Zahl ist größer als 0.\n");
}

printf("Hier gehts weiter\n");

return 0;
}