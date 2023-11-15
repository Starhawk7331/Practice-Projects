#include <stdio.h>

void main();
int Factorial(n);

void main(){
    int n;

    scanf("%d",&n);
    printf("%d",Factorial(n));
}
int Factorial(n){

    int Factor = 1;

    for(int i = 1;i <= n;i++){
        Factor = Factor * i;
    }
    return Factor;
}