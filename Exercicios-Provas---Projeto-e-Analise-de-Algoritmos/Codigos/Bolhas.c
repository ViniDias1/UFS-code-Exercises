#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


// apos a primeira prova tentei resolver essa questao de outras maneiras e uma das possiveis for pelo MERGE
// adaptei para caber na questao e a ideia segue a mesma, contando a quantidade de trocas feitas para determinar o vencedor
// tambem levei o codigo do merge que fiz na primeira prova



int mergeBolhas(int vetor[], int temp[], int meio, int direita, int esquerda) {

    int i = esquerda;
    int j = meio + 1;
    int k = esquerda;

    int contaTroca = 0;
    
    while (i <= meio && j <= direita) {

        if (vetor[i] <= vetor[j]) {
            temp[k] = vetor[i];
            k++;
            i++;
        } 
        else {
            temp[k] = vetor[j];
            k++;
            j++;
            contaTroca += meio - i + 1;
        }
    }
    
    while (i <= meio) {
        temp[k] = vetor[i];
        k++;
        i++;
    }
    
    while (j <= direita) {
        temp[k] = vetor[j];
        k++;
        j++;
    }
    
    for (i = esquerda; i <= direita; i++) {
        vetor[i] = temp[i];
    }
    
    return contaTroca;
}
int mergeSort(int vetor[], int temp[], int esquerda, int direita) {
    int contaTroca = 0;
    
    if (esquerda < direita) {

        int meio = (esquerda + direita) / 2;

        contaTroca += mergeSort(vetor, temp, esquerda, meio);
        contaTroca += mergeSort(vetor, temp, meio + 1, direita);
        contaTroca += mergeBolhas(vetor, temp, meio, direita, esquerda);
    }
    
    return contaTroca;
}

int main() {

    int n;
    
    while (1) {

        scanf("%d", &n);

        if (n == 0) break;
        
        int vetor[n], temp[n];
        int i;
        for (i = 0; i < n; i++) {
            scanf("%d", &vetor[i]);
        }
        
        int contaTroca = mergeSort(vetor, temp, 0, n - 1);
        
        if (contaTroca % 2 == 0) {
            printf("Carlos\n");
        } 
        else {
            printf("Marcelo\n");
        }
    }
    
    return 0;
}
