#include <stdio.h>

#define ARR_SIZE 98

void main(){

    int primes[ARR_SIZE];

    for(int i = 0;i < ARR_SIZE;i++){
        primes[i] = i + 2;
    }
    
    for(int i = 0;i < ARR_SIZE;i++){
        if(primes[i] != 0){
            for(int j = i+1;j < ARR_SIZE;j++){
                if(primes[j]%primes[i] == 0){
                    primes[j] = 0;
                }
            }
        }
    }

    for(int i = 0; i< ARR_SIZE;i++){
        if(primes[i] != 0){
            printf("%d ", primes[i]);
        }
    }
}