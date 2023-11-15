#include <stdio.h>

//Die Funktion powerof wird deklariert
int powerof(int a);

int main(){
    //Die for-schleife wiederholt den Aufruf der Funktion und ehöht i um 1
    for(int i=0;i<10;i++){
        printf("%d\n",powerof(i));
    }

}

int powerof(int a){
    //Die Variable result wierd deklariert und den wert von a*a zugewiessen
    int result=a*a;

    //result wird zurückgegebeen
    return result;
}