#include <stdio.h>
#include "speed.h"

//double getspeed(int time,int distance);



void main(){

    int time,dis;

    printf("Wie viel Zeit ist vergangen?");
    scanf("%d",&time);
    

    do{
        printf("Wie lang ist die Strecke");
        scanf("%d",&dis);
        
    }while(dis < 0);

    printf("%lf",getspeed(time,dis));
}

double getspeed(int time,int distance){

    if(time != 0){
        return distance / time;
    }
    else{
        return 0;
    }
}