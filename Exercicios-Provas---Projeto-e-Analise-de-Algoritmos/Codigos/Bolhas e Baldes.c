#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int bubbleSort(int vetor[], int tamanho){

	int aux, i, j;
    int trocas = 0;

	for(j = tamanho - 1; j >= 1; j--){

		for(i=0; i<j; i++){

			if(vetor[i] > vetor[i+1]){

				aux = vetor[i];
                vetor[i] = vetor[i+1];
                vetor[i+1] = aux;
                trocas++;
                
            }
        }
    }
    return trocas;
}

int main() {

    int v;
    int tamanho = 1;
    scanf("%i",&tamanho);       
    while (tamanho != 0){
        
        int vetor[tamanho];

        for (v = 0; v<tamanho; v++){
            scanf("%i",&vetor[v]);
        }

        // a inten�ao do bubble sort, nesse caso, eh saber quantas trocas foram realizadas na ordena�ao

        // como cada jogada eh intercalada com os dois jogadores, comparando se o numero de trocas eh par, impar ou 0 � possivel
        // descobrir o vencedor

        int trocaFinal = bubbleSort(vetor,tamanho);

        if (trocaFinal % 2 == 0 || trocaFinal == 0){
            printf("Carlos\n");
        }
        else{
            printf("Marcelo\n");
        }

        scanf("%i",&tamanho);
    }

	return 0;
}


// 1 5 3 4 2 
// 1 3 5 4 2 #1
// 1 3 5 2 4 #2
// 1 3 2 5 4 #3
// 1 2 3 5 4 #4
// 1 2 3 4 5 #5
