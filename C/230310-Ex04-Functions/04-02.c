#include <stdio.h>

//Die Funktion absoluteValue wird deklariert
int absoluteValue(a);

int main(){
    //absoluteValue wird aufgerufen und der Rückgabewert wird ausgegeben
    printf("%d", absoluteValue(-3));
}

int absoluteValue(a){
    //Überprüft ob a positiv ist
    if(a>0){
        //a wird zurückgegeben
        return a;
    }
    else{
        //a wird  positiv gemacht und zurückgegeben
        a = a * -1;
        return a;
    }
}