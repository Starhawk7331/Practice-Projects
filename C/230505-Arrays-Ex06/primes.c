#include <stdio.h>

void main(){
    
    int primes[98];

    for(int i = 2;i < 101; i++){
        primes[i-2] = i;
    }

    for(int i = 0; i<99;i++){
        if(primes[i] != 0){
            for(int j=i+1;j < 99;j++){
                if(primes[j]%primes[i] == 0){
                    primes[j] = 0;
                }
            }
        }
    }
    for(int i = 0;i <98; i++){
        if(primes[i] != 0){
            printf("%d ",primes[i]);
        }
    }
}