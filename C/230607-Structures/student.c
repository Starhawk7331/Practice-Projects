#include <stdio.h>

typedef struct{
    char name[100];
    long ID;
    int yearofbirth;
}student;

void printStudentInfo(student s);

void main(){

    student Karl = { "Karl",123456,1990};
    student otto = {" Otto",2222,2070};
   
    student Anna = {"Annerle"};
    Anna.ID = 9999;
    Anna.yearofbirth = 2005;

    printStudentInfo(Karl);
    printStudentInfo(otto);
    printStudentInfo(Anna);

    getchar();

}

void printStudentInfo(student s){
    printf("Name: %s / ID: %d / year: %d\n", s.name, s.ID, s.yearofbirth);
}