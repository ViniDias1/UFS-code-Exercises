#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
 
typedef struct 
{
    int valor;
    int indice;
 
}valorINDICE;
 
int main(){
 
    int tamanhoEntrada1,tamanhoEntrada2,i,j;
    int help = 0,aux = 0;
    scanf("%i %i",&tamanhoEntrada1,&tamanhoEntrada2);
    int vetorCOLORaux[tamanhoEntrada1], vetorQUERIESaux[tamanhoEntrada2];
    valorINDICE vetor[51];
    int indiceAUX = 0;
    
    for (i = 0; i< tamanhoEntrada1; i++){
        scanf("%i",&vetorCOLORaux[i]);
        if (i <=  51){
            
            vetor[i].indice = 0;
            vetor[i].valor = 0;
            indiceAUX++;
            
        }
    }
 
    for (i = 0; i< tamanhoEntrada2; i++){
        scanf("%i",&vetorQUERIESaux[i]);
    }
 
    for ( i = 0; i < tamanhoEntrada1; i++){
        int add = 0;
        aux = vetorCOLORaux[i];
        for (j = 0; j < indiceAUX - 1; j++){
 
            if(aux != vetor[j].valor ){
                add = 1;
            }
            else{
                add = -1;
                break;
            }
        }
 
        if (add == 1){
            vetor[help].valor = aux;
            vetor[help].indice = i+1;
            help++;
        }
            
    }
        
    for ( i = 0; i < tamanhoEntrada2; i++){
 
        int k = 0;
        valorINDICE temp;
 
        while (vetor[k].valor != vetorQUERIESaux[i]){
            k++;
        }
        
        printf("%i ",vetor[k].indice);
 
        if (vetor[k].indice != 1){
 
            while (k >= 1){
                
                temp = vetor[k-1];
                vetor[k-1] = vetor[k];
                vetor[k] = temp;
                vetor[k].indice = vetor[k].indice + 1;
                k--;
            }
 
            vetor[k].indice = 1;
        }
    }
    return 0;
}