#include <stdio.h>


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
