#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

// Nome: VINICIUS DIAS VALEN�A
// Matricula: 202100045850

// Essa questao ja tinha sido feita por mim ao tentar resolver a questao "GRANDE PROMO??O" que foi passada
//em uma atividade anterior a essa prova.

// a ideia consiste em rodar a funcao mochila para cada pessoa da familia levando em cosidera??o o peso maximo 
//que conseguem levar.
// incrementando esse valor a cada pessoa (seu peso maximo) que eh calculada, temos os valor maximo.



int max(int a, int b) {
    if (a > b){
        return a;
    }
    return b;
}


int mochila(int itens, int valores[], int pesos[], int capacidade) {

    int i, j;
    int tabela[itens + 1][capacidade + 1];

    for (i = 0; i <= itens; i++) {
        for (j = 0; j <= capacidade; j++) {

            if (i == 0 || j == 0) {
                tabela[i][j] = 0;
            }
            else if (pesos[i - 1] <= j) {
                tabela[i][j] = max(valores[i - 1] + tabela[i - 1][j - pesos[i - 1]], tabela[i - 1][j]);
            }
            else {
                tabela[i][j] = tabela[i - 1][j];
            }
        }
    }

    return tabela[itens][capacidade];
}

int main() {

    int casos;
    scanf("%d",&casos);

    while (casos > 0){
        int itens, capacidade, i;
        int familia;
        int respostaFINAL = 0;
        scanf("%d", &itens);

        int valores[itens] , pesos[itens];
        
        for (i = 0; i < itens; i++) {
            scanf("%d %d", &valores[i],&pesos[i]);
        }
        
        scanf("%d", &familia);

        for (i = 0; i < familia; i++){
            scanf("%d", &capacidade);
            respostaFINAL += mochila(itens,valores,pesos,capacidade);
        }
        
        printf("%d\n",respostaFINAL);
        casos--;

    }
     

    
    return 0;
}
