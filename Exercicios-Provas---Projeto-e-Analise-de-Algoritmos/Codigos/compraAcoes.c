
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int max(int a, int b) {
    if (a > b){
        return a;

    }
    return b;
}

int main() {
    int n,i;
    scanf("%d", &n);

    int precos[n];
    for (i = 0; i < n; i++) {
        scanf("%d", &precos[i]);
    }

    int menorPreco = precos[0];
    int lucroMAX = 0;

    for (i = 1; i < n; i++) {

        lucroMAX = max(lucroMAX, precos[i] - menorPreco);

        if (menorPreco > precos[i]){
            menorPreco = precos[i];
        }
    }

    printf("%d\n", lucroMAX);

    return 0;
}
