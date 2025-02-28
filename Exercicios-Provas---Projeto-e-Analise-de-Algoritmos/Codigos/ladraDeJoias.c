#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int max(int a, int b) {
    if (a>b){
        return a;
    }
    return b;
}

int verificacao(int* joias, int n, int* tabela) {
    
    if (n < 0){
        return 0;
    }
        

    if (tabela[n] != -1){
        return tabela[n];
    }

    int naoPegou = verificacao(joias, n - 1, tabela);
    int pegou = joias[n];

    if (n >= 2) {
        pegou += verificacao(joias, n - 3, tabela);
    } 

    else{
        if (n == 1) {
            pegou += verificacao(joias, n - 2, tabela);
        } 
    }

    int resultado = max(pegou, naoPegou);
    tabela[n] = resultado;

    return resultado;
}


int main() {
    int n;
    scanf("%d",&n);

    int tabela[n];
    int joias[n];
    int i;

    for ( i = 0; i < n; i++){
        scanf("%d",&joias[i]);
        tabela[i] = -1;
    }
    

    printf("%d", verificacao(joias, n - 1, tabela));
    return 0;
}
