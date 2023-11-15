#include <stdio.h>

#define SINGERS 4

void main();
void draw_Poles(int VotesSum,int VotesSingers[]);

void main(){

    int VotesSingers[SINGERS];
    

    int VotesSum = 0;

    for(int i=0;i<SINGERS;i++){
        printf("Wie viele Wahlen hat Saenger %d\n",i+1);
        scanf("%d",&VotesSingers[i]);
        VotesSum = VotesSum + VotesSingers[i];
    }

    draw_Poles(VotesSum,VotesSingers);

}

void draw_Poles(int VotesSum,int VotesSingers[]){

    int VotesPercent[SINGERS];

    for(int i=0;i<SINGERS;i++){
        VotesPercent[i] = (VotesSingers[i] *100) / VotesSum;
    }

    for(int i=0;i<SINGERS;i++){
        printf("Saenger %d: ",i);

        for(int n=0;n <= VotesPercent[i];n++){
            printf("*");
        }
        printf("\n");
    }
}