#include <stdio.h>

void main(){

    int a,b,sum,diff,product;
    double qoutient;
   
    printf("Geben Sie eine Zahl ein");
    scanf("%d",&a);getchar();

    printf("Geben Sie eine Zahl ein");
    scanf("%d",&b);getchar();

    if(b=0){
        printf("Mann kann nicht durch 0 dividieren");
    }
    else{
        sum=a+b;
        diff=a-b;
        product=a*b;
        qoutient=a/b;
        printf("Sum: %d\nDifference: %d\nProduct: %d\nQoutient: %lf",sum,diff,product,qoutient);
    }

}