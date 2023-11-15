#ifndef _SPEED_H_
#define _SPEED_H

#include <stdio.h>


double getspeed(int time,int distance){

    if(time != 0){
        return distance / time;
    }
    else{
        return 0;
    }
}