#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//inicilizar os dois vetores
//so ordenar se: 1. o indice do numero for TRUE e ele for maior que o indice + 1
// verifica se algo nao esta ordenado e define a resposta


typedef struct {
    int numero;
    bool troca;
};


int main(){

    int numCasosTeste;
    scanf("%i", &numCasosTeste);

    while (numCasosTeste > 0){
        
        int quantElementosVETOR,quantElementosPOSICAO;
        scanf("%i %i",&quantElementosVETOR,&quantElementosPOSICAO);
        
        int vetor[quantElementosVETOR];
        bool posicao[quantElementosVETOR];

        int i,indice;


        for (i = 0; i < quantElementosVETOR; i++){
            scanf("%i",&vetor[i]);
            posicao[i] = false;
        }

        for (i = 0; i < quantElementosPOSICAO; i++){
            
            scanf("%i",&indice);
            posicao[indice - 1] = true;
        }


        while (true){

            bool check = false;
            int temp;


            for ( i = 0; i < quantElementosVETOR; i++){

                if (posicao[i] && vetor[i] > vetor[i+1]){
                    
                    check = true;
                    temp = vetor[i];
                    vetor[i] = vetor[i+1];
                    vetor[i+1] = temp;
                }
            }
            
            if (!check){
                break;
            }
        }

        bool check = true;
        for (i = 0; i < quantElementosVETOR - 1;i++){

            if (vetor[i] > vetor[i+1]) {
                check = false;
                break;
            }
        }

        if (check) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
        
        numCasosTeste--;
    }
    return 0;
}