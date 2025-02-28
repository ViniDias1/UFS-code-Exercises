#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// "-" = RUIM = nao modifica
// "." = BOA = modifica depois de verificar sua posicao
// para garantir que dois nao possuam a mesma cor == (PAR = 'B') e (IMPAR = 'w')

// A ideia da solucao eh percorrer cada indice e verificar se eh modificavel ou nao e verificar se será B ou W 


int main(){
    
    int linha,coluna,i,j;

    scanf("%i %i", &linha,&coluna);

    char tabuleiro[linha][coluna];

    for ( i = 0; i < linha; i++){
        for ( j = 0; j < coluna; j++){

            scanf(" %c",&tabuleiro[i][j]);

            if (tabuleiro[i][j] == '.' ){

                if((j + i) % 2 == 0){
                    tabuleiro[i][j] = 'B';
                }
                else{
                    tabuleiro[i][j] = 'W';
                }
            }
            printf("%c",tabuleiro[i][j]);
        }
        printf("\n");
    }

    // retirei o for para ser mais rapido. 

    return 0;
}
