#include <stdio.h>

void main();
int diffference(a,b);


void main(){
    int a =5;
    int b =5;
    printf("%d",difference(a,b));
}

int difference(a,b){
    if(a == b){
        return 0;
    }
    else if(a > b){
        return 1;
    }
    else{
        return -1;
    }

}