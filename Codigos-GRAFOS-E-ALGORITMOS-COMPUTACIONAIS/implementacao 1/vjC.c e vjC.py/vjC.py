
# essa implementacao foi baseado no codigo feito originalmente em C. Provavelmente, a funcao qsort() esta causando problema e o tempo
# de execucao esta estourando.

# Decidi fazer em python e a questao foi aceita. 
 
numeroDePessoas = int(input())

vetor = []
maximoVIVOS = 0
maximoANO = 0
vivos = 0

for i in range(numeroDePessoas):
   
    nasce,morre = map(int,input().split())
    vetor.append([nasce,1])
    vetor.append([morre,-1])

vetor = sorted(vetor)

for i in range(2*numeroDePessoas):

    vivos += vetor[i][1]
    
    if  vivos > maximoVIVOS:
        maximoVIVOS = vivos
        maximoANO = vetor[i][0]

print(maximoANO,maximoVIVOS)



# implementacao em C

"""
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// implementação em C do YEARS

typedef struct {
    
    int ano;
    bool morte;

}ANOeMORTE;

// eh preciso ordenar em relacao aos booleanos tambem 

int comparar(const void *a, const void *b){

    if (*(int*)a == *(int*)b){

        if (*(bool*)a == true && *(bool*)b == false){
            return 1;
        }
        if (*(bool*)a == false && *(bool*)b == false){
            return -1;
        }
        
        return 0;
    }
    else{
        if (*(int*) a < *(int*)b){
            return -1;
        }
        else{
            return 1;
        }

    }

}


int main(){

    int numeroDePessoas,i;
    scanf("%i", &numeroDePessoas);
    ANOeMORTE vetor[numeroDePessoas*2];
    int nasce,morre,temp,indice;
    ANOeMORTE *point = vetor;

    temp = numeroDePessoas;


    while(temp > 0) {

        ANOeMORTE am1,am2;
        scanf("%i %i", &nasce, &morre);
        
        am1.ano = nasce;
        am1.morte = false;

        am2.ano = morre;
        am2.morte = true;

        vetor[indice] = am1;
        indice++;
        vetor[indice] = am2;
        indice++;

        temp--;

    }

    qsort(point,numeroDePessoas*2,sizeof(ANOeMORTE),comparar);
    
    int vivos = 0;
    int maximoVIVOS = 0;
    int maximoANO = 0;
    int add;
    for (i = 0; i < numeroDePessoas*2; i++) {

        if (vetor[i].morte){
            add = -1;
        }
        else{
            add = 1;
        }

        vivos = vivos + add;

        if (vivos > maximoVIVOS){
            maximoVIVOS = vivos;
            maximoANO = vetor[i].ano;
        }
    }

    printf("%i %i", maximoANO,maximoVIVOS);

    return 0;
}

"""