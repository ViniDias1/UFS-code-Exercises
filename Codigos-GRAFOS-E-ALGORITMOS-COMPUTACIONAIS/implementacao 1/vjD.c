#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int topo = -1;

// a ideia eh tentar encontrar um equilibrio entre ABERTOS "(" e FECHADOS ")".
// da pra usar pilha

bool vazio(char pilha[]){
    if (pilha[0] != '(' && pilha[0] != ')'){
        return true;
    }
    return false;
}

void inserir(char carac,char pilha[],int tamanho){

    if (topo == tamanho){
        return;
    }
    topo++;
    pilha[topo] = carac;
    return;
}

void remover(char pilha[]){

    pilha[topo] = 'x';
    topo--;
}


int main(){

    int tamanho,i;     
    bool opa = false;    

    scanf("%i",&tamanho);
    char pilha[tamanho];
    char string[tamanho]; 
    scanf("%s",&string);

    for ( i = 0; i < tamanho; i++){

        if (string[i] == '('){
            inserir(string[i],pilha,tamanho);
        }

        else{

            if (!vazio(pilha) && pilha[topo] == '('){
                remover(pilha);
            }
            else{
                inserir(string[i],pilha,tamanho);
            }
        }

        if (!vazio(pilha) && pilha[topo] == ')' && !opa){
            remover(pilha);
            opa = true;
        }
        
    }

    if (!opa && topo == -1) {
        printf("YES");
    }

    else {
        

        if (opa && topo == 0 && pilha[topo] == '(') {
            printf("YES");
        } 

        else {
            printf("NO");
        }  
    }
    return 0;


}