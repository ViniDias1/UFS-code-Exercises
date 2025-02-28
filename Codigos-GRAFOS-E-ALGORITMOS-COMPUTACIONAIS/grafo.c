// Nome: Vincius Dias Valenca
//Matricula: 202100045850
//Data de finalizacao: 25/02/2023

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Criar um grafo (x) 
// Criar um vertice e adicionar ao grafo (x)
// Adicionar aresta (x)
// Remover vertice (x) 
// Remover aresta (x)
// Grau de um vertice (x) 
// Se dois vertices sao vizinhos (x)
// Se tem ciclo euleriano (x)


typedef struct Node {

    int vertice;
    struct Node* prox;

} Node;


typedef struct Grafo {

    int numeroVertices;
    Node** listaAdjacencia;

} Grafo;


Node* cria_node(int v) {

    Node* novoNode = (Node*) malloc(sizeof(Node));
    novoNode->vertice = v;
    novoNode->prox = NULL;

    return novoNode;

}


Grafo* cria_grafo(int numeroVertices) {

    Grafo* grafo = (Grafo*) malloc(sizeof(Grafo));
    grafo->numeroVertices = numeroVertices;
    grafo->listaAdjacencia = (Node**) malloc(numeroVertices * sizeof(Node*));
    int i;
    
    for (i = 0; i < numeroVertices; i++) {
        grafo->listaAdjacencia[i] = NULL;
    }

    return grafo;
}


void adicionaVertice(Grafo* grafo) {

    int novoNumVertices = grafo->numeroVertices + 1;
    Node** novaListaAdjacencia = (Node**) malloc(novoNumVertices * sizeof(Node*));
    int i;


    for (i = 0; i < grafo->numeroVertices; i++) {
        novaListaAdjacencia[i] = grafo->listaAdjacencia[i];
    }

    novaListaAdjacencia[novoNumVertices - 1] = NULL;


    free(grafo->listaAdjacencia);
    grafo->listaAdjacencia = novaListaAdjacencia;
    grafo->numeroVertices = novoNumVertices;
}




void adicionaAresta(Grafo* grafo, int vA, int vB) {

    Node* novoNode = cria_node(vB);
    novoNode->prox = grafo->listaAdjacencia[vA];
    grafo->listaAdjacencia[vA] = novoNode;


    novoNode = cria_node(vA);
    novoNode->prox = grafo->listaAdjacencia[vB];
    grafo->listaAdjacencia[vB] = novoNode;
}



// Function to remove an edge from the grafo
void removeAresta(Grafo* grafo, int vA, int vB) {
    Node* atual = grafo->listaAdjacencia[vA];
    Node* anterior = NULL;


    while (atual != NULL && atual->vertice != vB) {
        anterior = atual;
        atual = atual->prox;
    }


    if (atual != NULL) {
        if (anterior == NULL) {
            grafo->listaAdjacencia[vA] = atual->prox;
        } 
        else {
            anterior->prox = atual->prox;
        }
        free(atual);
    }


    atual = grafo->listaAdjacencia[vB];
    anterior = NULL;
    while (atual != NULL && atual->vertice != vA) {
        anterior = atual;
        atual = atual->prox;
    }

    if (atual != NULL) {
        if (anterior == NULL) {
            grafo->listaAdjacencia[vB] = atual->prox;
        } else {
            anterior->prox = atual->prox;
        }
        free(atual);
    }
}


void removeVertice(Grafo* grafo, int vertice) {

    int i;
    for (i = 0; i < grafo->numeroVertices; i++) {

        if (i == vertice) {
            continue;
        }

        Node* anterior = NULL;
        Node* atual = grafo->listaAdjacencia[i];

        while (atual != NULL) {
            if (atual->vertice == vertice) {
                if (anterior == NULL) {
                    grafo->listaAdjacencia[i] = atual->prox;
                } else {
                    anterior->prox = atual->prox;
                }

                free(atual);
                break;
            }

            anterior = atual;
            atual = atual->prox;
        }
    }


    Node* atual = grafo->listaAdjacencia[vertice];
    while (atual != NULL) {
        Node* temp = atual;
        atual = atual->prox;
        free(temp);
    }


    grafo->listaAdjacencia[vertice] = NULL;
}


int grau(Grafo* grafo, int v) {
    Node* atual = grafo->listaAdjacencia[v];
    int grau = 0;

    
    while (atual != NULL) {
        grau++;
        atual = atual->prox;
    }

    return grau;
}


bool isVizinho(Grafo* grafo, int v1, int v2) {
    Node* atual = grafo->listaAdjacencia[v1];


    
    while (atual != NULL) {
        if (atual->vertice == v2) {
            return true;
        }
        atual = atual->prox;
    }

    return false;
}


bool cicloEuleriano(Grafo* grafo) {
    
    int i;
    for (i = 0; i < grafo->numeroVertices; i++) {
        if (grau(grafo, i) % 2 != 0) {
            return false;
        }
    }

    return true;
}



void print_grafo(Grafo* grafo) {
    int i;
    for (i = 0; i < grafo->numeroVertices; i++) {
        
        Node* temp = grafo->listaAdjacencia[i];
        printf("Vertice %d: ", i);

        while (temp) {
            printf("%d -> ", temp->vertice);
            temp = temp->prox;
        }
        printf("NULL\n");
    }
}

int main() {
    
    int entradaVertices;
    int opcao = 0;
    int vertA;
    int vertB;
    int grauVertice;
    bool vizinho;
    bool cEuleriano;


    do{
        printf("\n");
        printf("1. Criar grafo\n");
        printf("2. Adicionar vertice\n");
        printf("3. Adicionar aresta\n");
        printf("4. Remover vertice\n");
        printf("5. Remover aresta\n");
        printf("6. Grau de um vertice\n");
        printf("7. Verificar se são vizinhos\n");
        printf("8. Verificar se o grafo possui ciclo Euleriano\n");
        printf("9. Imprimir lista de adjacencia\n");
        printf("10. Sair\n");

        printf("Escolha uma opcao: ");
        scanf("%d",&opcao);
    
        

        switch (opcao){

            case 1:
                //Criar grafo
                printf("Quantos vertices terá o grafo?: ");
                scanf("%d", &entradaVertices);
                Grafo* grafo = cria_grafo(entradaVertices);
                printf("\nGrafo criado\n\n");
                printf("--------------------\n");
                break;

            case 2:
                adicionaVertice(grafo);
                printf("Um vertice foi adicionada ao grafo\n\n");
                printf("--------------------\n");
                break;

            case 3:
                printf("Quais dois vertices deseja conectar?: ");
                scanf("%d %d", &vertA, &vertB);
                adicionaAresta(grafo,vertA,vertB);
                printf("Uma aresta foi adicionada entre esses dois vertices\n\n");
                printf("--------------------\n");
                break;

            case 4:
                printf("Qual vertice remover?: ");
                scanf("%d", &vertA);
                removeVertice(grafo,vertA);
                printf("Vertice removido!\n\n");
                printf("--------------------\n");
                break;

            case 5:
                printf("Quais vertices estao na aresta escolhida?: ");
                scanf("%d %d", &vertA, &vertB);
                removeAresta(grafo,vertA,vertB);
                printf("\nUma aresta foi removida entre esses dois vertices\n\n");
                printf("--------------------\n");
                break;

            case 6:
                printf("Qual o vertice que deseja ver o grau?: ");
                scanf("%d", &vertA);

                grauVertice = grau(grafo,vertA);
            
                printf("\nO grau do vertice %d eh %d\n\n", vertA,grauVertice);
                printf("--------------------\n");
                break;

            case 7:
                printf("Quais vertices deseja ver se sao vizinhos?: ");
                scanf("%d %d", &vertA, &vertB);
                vizinho = isVizinho(grafo,vertA,vertB);
                if (vizinho){
                    printf("\nSao vizinho!\n\n");
                }
                else{
                    printf("\nNao sao vizinhos\n\n");
                }
                printf("--------------------\n");
                break;
            
            case 8:

                cEuleriano = cicloEuleriano(grafo);
                if (cEuleriano){
                    printf("\nPossui Ciclo Euleriano!\n\n");
                }
                else{
                    printf("\nNao possui Ciclo Euleriano\n\n");
                }
                printf("--------------------\n");
                break;
            case 9:
                print_grafo(grafo);
                printf("--------------------\n");
                break;

            default:
                printf("\n\nOpcao invalida. Tente novamente\n\n");
                printf("--------------------\n");
        }

    } while (opcao != 10);


    return 0;
}