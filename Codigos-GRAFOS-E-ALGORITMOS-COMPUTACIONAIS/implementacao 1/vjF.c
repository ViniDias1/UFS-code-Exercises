#include <stdio.h>

// comparando cada funcionario ate achar um com -1, irei incrementar

int main() {

    int numeroDeFuncionarios,i;
    scanf("%d", &numeroDeFuncionarios);

    int vetor[numeroDeFuncionarios];
    int grupo = 0;
    int cont = 0;
    int temp;

    for (i = 0; i < numeroDeFuncionarios; i++) {
        scanf("%i",&vetor[i]);
    }

    for ( i = 0; i < numeroDeFuncionarios; i++){

        int cont = 0;
        int temp;

        temp = vetor[i];

        while (temp != -1){
            temp = vetor[temp - 1];
            cont++;
        }


        if (cont > grupo){
            grupo = cont;
        }
        

    }

    printf("%i", grupo+1);
    
    return 0;

}