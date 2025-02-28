
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


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


// void adicionaVertice(Grafo* grafo) {

//     int novoNumVertices = grafo->numeroVertices + 1;
//     Node** novaListaAdjacencia = (Node**) malloc(novoNumVertices * sizeof(Node*));
//     int i;


//     for (i = 0; i < grafo->numeroVertices; i++) {
//         novaListaAdjacencia[i] = grafo->listaAdjacencia[i];
//     }

//     novaListaAdjacencia[novoNumVertices - 1] = NULL;


//     free(grafo->listaAdjacencia);
//     grafo->listaAdjacencia = novaListaAdjacencia;
//     grafo->numeroVertices = novoNumVertices;
// }




void adicionaAresta(Grafo* grafo, int vA, int vB) {

    Node* novoNode = cria_node(vA);
    novoNode->prox = grafo->listaAdjacencia[vB];
    grafo->listaAdjacencia[vB] = novoNode;


    // novoNode = cria_node(vA);
    // novoNode->prox = grafo->listaAdjacencia[vB];
    // grafo->listaAdjacencia[vB] = novoNode;
}




// void print_grafo(Grafo* grafo) {
//     int i;
//     for (i = 0; i < grafo->numeroVertices; i++) {
        
//         Node* temp = grafo->listaAdjacencia[i];
//         printf("Vertice %d: ", i+1);

//         while (temp) {
//             printf("%d -> ", temp->vertice+1);
//             temp = temp->prox;
//         }
//         printf("NULL\n");
//     }
// }

int entradaZero(Grafo* grafo,int numVertices) {
    int cont = 0;
    int i;

    for (i = 0;i<numVertices;i++){
        Node* vert = grafo->listaAdjacencia[i];
        
        if (!vert){
            cont++;
        }
        


    }
    

    return cont;
}

int main() {
    int numVertices,numArestas,raiz,i;
    int resposta = 0;

    scanf("%d %d %d",&numVertices,&numArestas,&raiz);
    Grafo* grafo = cria_grafo(numVertices);

    if (numArestas == 0){
        resposta = numVertices - 1;
        printf("%d", resposta);
        return 0;
    }
    

    for (i = 0; i<numArestas; i++){
        int v1,v2;
        scanf("%d %d",&v1,&v2);
        v1--;v2--;
        adicionaAresta(grafo,v1,v2);
    }
    // print_grafo(grafo);
    

    resposta = entradaZero(grafo,numVertices);
    printf("%d", resposta);

   
    return 0;
}