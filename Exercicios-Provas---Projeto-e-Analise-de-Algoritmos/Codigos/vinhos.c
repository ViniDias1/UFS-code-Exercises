#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int n;
int preco[300+1];
int resposta[300+1][300+1];

int max(int a, int b) {
    if (a > b){
        return a;
    }

    return b;
}

int tabela(int esq, int dir, int anos) {
    int esquerda,direita;
    
    if (esq > dir) {
        return 0;
    }

    if (resposta[esq][dir] != -1) {
        return resposta[esq][dir];
    }

    esquerda = preco[esq] * anos + tabela(esq+1, dir, anos+1);
    direita = preco[dir] * anos + tabela(esq, dir-1, anos+1);

    resposta[esq][dir] = max(esquerda, direita);

    return resposta[esq][dir];
}

int main() {
    

    while (scanf("%d", &n) != EOF) {  
        
        int i,j;
        for (i = 1; i <= n; i++) {
            scanf("%d", &preco[i]);
        }

        for (i = 0; i <= n; i++) {
            for (j = 0; j <= n; j++) {
                resposta[i][j] = -1;
            }
        }

        printf("%d\n", tabela(1, n, 1));
    }

    return 0;
}
