#include <stdio.h>

int main()
{

int i;

printf("Gebe Sie eine Zahl ein\n");

scanf("%d",&i);getchar();

if(i>0){

if(i%2==0){
printf("Die Zahl ist gerade\n");

}
else{
    printf("Die Zahl ist ungerade\n");
}

printf("Die Zahl ist größer als 0\n");
}
else{
printf("Die Zahl ist kleiner als 0\n");

}



return 0;
}