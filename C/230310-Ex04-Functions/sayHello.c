#include <stdio.h>


//Funktionen deklarieren
void sayHello(int count);
void say4hello();

int main(){
    sayHello(4);
    say4hello();

    return 0;
}

void sayHello(int count){
    for(int i=0; i<count; i++){
        printf("hello\n");
    }
} 

void say4hello(){
    sayHello(4);
}
