#include <stdio.h>

void main(){

    char board[8][8] = {
        {'T','S','L','D','K','L','S','T'},
        {'B','B','B','B','B','B','B','B'},
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'},
        {'b','b','b','b','b','b','b','b'},
        {'t','s','l','d','k','l','s','t'},
    };
    


    
    printf("* * * * * * * * * * * * *\n");
    printf("*    a b c d e f g h    *\n");
    printf("*    ________________   *\n");
    

    for(int r = 0;r < 8;r++){
        printf("* %d |",r+1);
        for(int c = 0;c < 8;c++){
            printf("%c ",board[r][c]);
        }
        printf("|  *\n");
    }
    printf("*   -----------------   *\n");
    printf("* * * * * * * * * * * * *");
}