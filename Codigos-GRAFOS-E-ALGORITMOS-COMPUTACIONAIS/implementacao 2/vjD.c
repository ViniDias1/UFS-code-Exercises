// usar o algoritmo de Floyd-Warshall 
#include <stdio.h>
#include <stdbool.h>
#include <limits.h>
#include <stdint.h>

// Nome: Vinicius Dias Valenca
// Matricula: 202100045850

// no caso teste 30, valores maiores do que o suportado pelo INT estavam sendo impressos e dando erro na reposta final
// por esse motivo usei o int64_t para que valores maiores passam ser impressos.

int main() {

    int64_t grafo[510][510] = {};
    int64_t deletados[510] = {};
    int64_t caminhos[510];
    int numeroVertices,i,j,s,w;

    while (scanf("%d", &numeroVertices) == 1) {

        for (i = 1; i <= numeroVertices; i++) {
            for (j = 1; j <= numeroVertices; j++) {
                scanf("%lld", &grafo[i][j]);
                caminhos[0] += grafo[i][j];
            }
        }

        for (i = numeroVertices; i >= 1; i--) {
            scanf("%lld", &deletados[i]);
        }

        bool verificadoDeletados[510] = {false};
        
        for (s = 1; s <= numeroVertices; s++) {
            
            w = deletados[s];
            verificadoDeletados[w] = true; // marca como deletado
            caminhos[s] = 0;

            for (i = 1; i <= numeroVertices; i++) {
                for (j = 1; j <= numeroVertices; j++) {

                    // se for o tamanho atual for maior == substitui.
                    // se nao == mantem.
                    if (grafo[i][j] > grafo[i][w] + grafo[w][j]){
                        grafo[i][j] = grafo[i][w] + grafo[w][j];
                    }
                    
                    if (verificadoDeletados[i] && verificadoDeletados[j]) {
                        caminhos[s] += grafo[i][j];
                    }
                }
            }
        }
        // imprimi de tras para frente 
        for (i = numeroVertices; i >= 1; i--) {
            printf("%lld ", caminhos[i]);
        }
        printf("\n");
    }
    return 0;
}