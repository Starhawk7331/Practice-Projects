#include <stdio.h>

int main()
{

int i;

printf("Geben Sie eine Zahl ein:");

scanf("%d",&i);getchar();

if(i % 2 == 0){
printf("Die Zahl ist gerade");

}
else{
printf("Die Zahl ist ungerade");
}


return 0;
}