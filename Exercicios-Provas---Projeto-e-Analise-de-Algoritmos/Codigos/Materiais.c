#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Nome: VINICIUS DIAS VALENCA
// Matricula: 202100045850

// Passo 1: Ordena com base no pre?o
// Passo 2: Percorro atualizando o troco. E mantenha uma variavel de controle para saber ate onde fui.
// Passo 3: Sabendo o indice do item limite, ordeno esse sub-parte do vetor em ordem alfabetica e imprimo.


typedef struct {
    char item[25];
    float preco;
} Item;

int main() {

    float dinheiro;
    int quantidadeItens,i,j;
    Item itens[100];

    int intensMAX = 0;
    

    scanf("%f", &dinheiro);
    scanf("%d", &quantidadeItens);
    
    float troco = dinheiro;
    
    for (i = 0; i < quantidadeItens; i++) {
        scanf("%s %f", itens[i].item, &itens[i].preco);
    }

    // arriscando o bubble sort, ja que a questao ? de 3s e tem no maximo 100 itens
    for (i = 0; i < quantidadeItens - 1; i++) {

        for (j = 0; j < quantidadeItens - i - 1; j++) {

            if (itens[j].preco > itens[j + 1].preco) {

                Item temp = itens[j];

                itens[j] = itens[j + 1];
                itens[j + 1] = temp;
            }
        }
    }


    for (i = 0; i < quantidadeItens; i++) {

        if (itens[i].preco <= troco) {
            intensMAX++;
            troco -= itens[i].preco;
        } 
        else {
            break;
        }
    }

    // Ordena os itens comprados em ordem alfab?tica usando bubble sort
    for (i = 0; i < intensMAX - 1; i++) {

        for (j = 0; j < intensMAX - i - 1; j++) {
            // esse jeito foi a forma mais simples que achei para ordenar em ordem alfabetica
            // usando strcmp
            if (strcmp(itens[j].item, itens[j + 1].item) > 0) {

                Item temp = itens[j];
                itens[j] = itens[j + 1];
                itens[j + 1] = temp;

            }
        }
    }

    
    for (i = 0; i < intensMAX; i++) {
        printf("%s %.2f\n", itens[i].item, itens[i].preco);
    }

    printf("%.2f\n", troco);

    return 0;
}
