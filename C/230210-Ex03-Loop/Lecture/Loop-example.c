#include <stdio.h>

void main(){

    //We want to use various Loops to write the numbers 1-10

    //WHILE

    int w=0;

    while (w<10){
        printf("%d",++w);
    }
    
    w=1;

    while (w<=10){
        printf("%d",w);
        w++;//w+=1; OR w=w+1;
    }
    
    //FOR

    for(int f=1;f<=10;f++/*f+=1 OR f=f+1*/){
        printf("%d",f);
    }

    int f;

    for(f=1;f<=10;f=f+1){
        printf("%d",f);
    }

    //Do-While

    int d=0;

    do{
        printf("%d",++d);
    }while(d<10);

    d=1;

    do
    {
        printf("%d",d);
        d++;
    } while (d<=10);
    
}