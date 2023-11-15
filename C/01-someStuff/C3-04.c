#include <stdio.h>

int main(){

int a,b,result,input;

a=3;
b=2;

printf("1. Addieren.\n");
printf("2. Multiplizieren.\n");
printf("3. Dividieren.\n");
printf("Ihre Auswahl: ");

scanf("%d", &input); getchar();

if(input==1){
result = a + b;
}
else if(input==2){
    result= a*b;
}
else if(input==3){
    result = a/b;
}
else{
    printf("Ungueltige Zahl");
}

printf("%d",result);

return 0;

}