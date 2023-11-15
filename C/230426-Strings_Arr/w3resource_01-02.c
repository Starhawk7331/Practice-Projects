/*
1. Write a program in C to input a string and print it. Go to the editor

Test Data :
Input the string : Welcome, w3resource

Expected Output :

The string you entered is : Welcome, w3resource 

2. Write a program in C to find the length of a string without using library functions. Go to the editor

Test Data :
Input the string : w3resource.com

Expected Output :

Length of the string is : 15
*/

#include <stdio.h>

#define input_size  

void main(){
    char input[100];

    printf("Please enter a string:\n");

    fgets(input,input_size,stdin);

    printf("The string you entered is: %s\n",input);

    for(int i= 0;i<= input_size;i++){

        if(input[i]== '\n'){
            input[i] = '\0';
            printf("The string is this long: %d",i);
            break;
            
        }
    }
}
