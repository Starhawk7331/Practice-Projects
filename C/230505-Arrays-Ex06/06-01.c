#include <stdio.h>

void main(){

    int fibonacci[15] = {0,1};

    for(int i = 2;i < 15;i++){
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2];
    }
    for(int i = 0;i<15;i++){
        printf("%d\n",fibonacci[i]);
    }
}