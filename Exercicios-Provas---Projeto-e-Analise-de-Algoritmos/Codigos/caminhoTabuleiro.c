#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define maximo 1000



int tabuleiro[maximo][maximo];
int tabela[maximo][maximo];
int caminho[maximo];

int min(int a, int b) {
    if (a < b){
        return a;
    }
    return b;
}

int main() {
    int n;
    scanf("%d", &n);
    int i,j;

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", &tabuleiro[i][j]);
        }
    }


    for (i = 0; i < n; i++) {
        tabela[n-1][i] = tabuleiro[n-1][i];
    }


    for (i = n-2; i >= 0; i--) {
        for (j = 0; j < n; j++) {
            tabela[i][j] = INT_MAX;

            if (j > 0 && tabela[i+1][j-1] != INT_MAX) {
                tabela[i][j] = min(tabela[i][j], tabela[i+1][j-1]);
            }

            tabela[i][j] = min(tabela[i][j], tabela[i+1][j]);

            if (j < n-1 && tabela[i+1][j+1] != INT_MAX) {
                tabela[i][j] = min(tabela[i][j], tabela[i+1][j+1]);
            }

            tabela[i][j] += tabuleiro[i][j];
        }
    }

    int menorCAMINHO = INT_MAX;
    int comeco;

    for (j = 0; j < n; j++) {
        if (tabela[0][j] < menorCAMINHO) {
            menorCAMINHO = tabela[0][j];
            comeco = j;
        }
    }

    i = 0;
    j = comeco;
    int tamanhoCaminho = 0;

    while (i < n-1) {

        caminho[tamanhoCaminho] = j;
        
        tamanhoCaminho++;
        
        if (j > 0 && tabela[i+1][j-1] == tabela[i][j] - tabuleiro[i][j]) {
            j--;
        } 
        else {
            if (j < n-1 && tabela[i+1][j] == tabela[i][j] - tabuleiro[i][j]){
                j = j;
            }
            else{
                if (j < n-1 && tabela[i+1][j+1] == tabela[i][j] - tabuleiro[i][j]) {
                    j++;
                }
            }
            
        }
        i++;
        
    }

    
    printf("%d\n", menorCAMINHO);
    printf("[%d,%d]", n-1, j);
    int k;

    for (k = tamanhoCaminho - 1; k >= 0; k--) {
        printf(" <- [%d,%d]", k, caminho[k]);
    }
    printf("\n");

    return 0;
}
