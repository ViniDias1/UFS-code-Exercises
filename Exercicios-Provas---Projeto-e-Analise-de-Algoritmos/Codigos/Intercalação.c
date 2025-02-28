#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {


    // codigo com while 

    int sizeLista1, sizeLista2, i, j, k;
    scanf("%d", &sizeLista1);
    scanf("%d", &sizeLista2);
    int indiceVT1 = 0, indiceVT2 = 0, indiceFINAL = 0;
    int tamanhoVetorFinal = sizeLista1 + sizeLista2;
    int vetor1[sizeLista1], vetor2[sizeLista2], vetorFINAL[tamanhoVetorFinal];

    for (i = 0;i < sizeLista1;i++) {
        scanf("%d", &vetor1[i]);
    }
    for (j = 0; j < sizeLista2; j++) {
        scanf("%d", &vetor2[j]);
    }

    while (indiceVT1 < sizeLista1 && indiceVT2 < sizeLista2) {

        if (vetor1[indiceVT1] <= vetor2[indiceVT2]) {
            vetorFINAL[indiceFINAL] = vetor1[indiceVT1];
            indiceVT1++;
        } else {
            vetorFINAL[indiceFINAL] = vetor2[indiceVT2];
            indiceVT2++;
        }

        indiceFINAL++;
    }


    while (indiceVT1 < sizeLista1) {
        vetorFINAL[indiceFINAL] = vetor1[indiceVT1];
        indiceVT1++;
        indiceFINAL++;
    }


    while (indiceVT2 < sizeLista2) {
        vetorFINAL[indiceFINAL] = vetor2[indiceVT2];
        indiceVT2++;
        indiceFINAL++;
    }

    for (i = 0;i < tamanhoVetorFinal;i++) {
        printf("%d\n", vetorFINAL[i]);
    }

    return 0;
}
