#include <stdio.h>
#include <stdlib.h>

//---------------------
#define MAXN 100

int heap[MAXN];
int tamanho_heap;
//---------------------

int pai(int i){
    return i/2;
}

int esquerda(int i){
    return 2*i;
}

int direita(int i){
    return 2*i+1;
}

// STRING
// int comparar(const void *a, const void *b) {
//     const char **str_a = (const char **)a;
//     const char **str_b = (const char **)b;
    
//     return strcmp(*str_a, *str_b);
// }

// CHAR
// int comparar(const void *a, const void *b) {
//     const char *char_a = (const char *)a;
//     const char *char_b = (const char *)b;
    
//     return (*char_a - *char_b);
// }

// INTEIROS
// int comparar(void* a, void* b){
//     
//     int* ptr_a = (int*) a;
//     int* ptr_b = (int*) b;
//     if (*ptr_a < *ptr_b) return -1;
//     if (*ptr_a > *ptr_b) return 1;
//     return 0;
// }



void heapify_up(int v){
    
    if(v == 1){
        return;
    } 
    
    int p = pai(v);
    if(heap[v] > heap[p]){
        int tmp = heap[v];
        heap[v] = heap[p];
        heap[p] = tmp;
        
        heapify_up(p);
    }
    
}

void heapify_down(int v){
    
    int d = direita(v);
    int e = esquerda(v);
    
    int maior = v;
    
    if(d <= tamanho_heap && heap[d] > heap[maior]){
       maior = d; 
    } 
    if(e <= tamanho_heap && heap[e] > heap[maior]){
        maior = e;
    } 
    
    
    if(maior != v){
        int tmp = heap[v];
        heap[v] = heap[maior];
        heap[maior] = tmp;
        
        heapify_down(maior);
    }
}

void insere(int valor){
    heap[++tamanho_heap] = valor;
    
    heapify_up(tamanho_heap);
}

void deleta(int posicao){
    
    int tmp = heap[posicao];
    heap[posicao] = heap[tamanho_heap];
    heap[tamanho_heap] = tmp;
    
    tamanho_heap--;
    
    heapify_down(posicao);
}

void heapsort(int *vetor, int tamanho){
    // Transforma o vetor em um heap
    for(int i=0; i<tamanho; i++){
        insere(vetor[i]);
    }
    
    // Remove os elementos do heap na ordem correta (ascendente)
    for(int i=tamanho-1; i>=0; i--){
        vetor[i] = heap[1];
        deleta(1);
    }
}

int main(){
    // Exemplo de uso:
    
    int vetor[] = {5, 1, 4, 2, 3};
    int tamanho = sizeof(vetor)/sizeof(vetor[0]);
    
    heapsort(vetor, tamanho);
    
    // Imprime o vetor ordenado
    for(int i=0; i<tamanho; i++){
        printf("%d ", vetor[i]);
    }
    printf("\n");
    
    return 0;
}
