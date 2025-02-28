#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Nome: Vinicius Dias Valenca
// Matricula: 202100045850

void computaTabela(char* padrao, int tamanhoPadrao, int shifts[]) {
    int i, last;

    for (i = 0; i < 256; i++) {

        shifts[i] = tamanhoPadrao;

    }

    for (i = 0; i < tamanhoPadrao - 1; i++) {

        last = (int)padrao[i];
        shifts[last] = tamanhoPadrao - i - 1;

    }
}

void horspool(char* texto, int textoTamanho, char* padrao, int tamanhoPadrao) {

    int i = tamanhoPadrao - 1, j, last;
    int shifts[256];

    computaTabela(padrao, tamanhoPadrao, shifts);
    int x = 0;

    while (i < textoTamanho) {

        last = (int)texto[i];

        if (last == (int)padrao[tamanhoPadrao - 1]) {

            j = tamanhoPadrao - 2;

            while (j >= 0 && texto[i - tamanhoPadrao + 1 + j] == padrao[j]) {
                j--;
            }

            if (j == -1) {
                printf("%d\n", i - tamanhoPadrao + 1);
                x = 1;
                i++;
            } 

            else {
                i += shifts[last];
            }

        } 

        else {
            i += shifts[last];
        }
    }
    if (x == 0){
       printf("-1"); 
       return;
    }
    
}

int main() {
    char texto[7000000];
    char padrao[1000000];
    int textoTamanho, tamanhoPadrao, pos;

    scanf("%s", texto);
    scanf("%s", padrao);

    textoTamanho = strlen(texto);
    tamanhoPadrao = strlen(padrao);

    horspool(texto, textoTamanho, padrao, tamanhoPadrao);
    
    return 0;
}
