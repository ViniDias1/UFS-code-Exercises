#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

typedef struct consulta {
    int inicio;
    int fim;
} consulta;

// funcao que ja tinha pronta
int compara(const void *a, const void *b) {

    consulta *consulta1 = (consulta*)a;
    consulta *consulta2 = (consulta*)b;
    
    return (consulta1->fim - consulta2->fim);
}

int main() {
    int n;
    scanf("%d", &n);

    consulta consultas[n];
    int i;
    for (i = 0; i < n; i++) {
        scanf("%d %d", &consultas[i].inicio, &consultas[i].fim);
    }

    qsort(consultas, n, sizeof(consulta), compara);

    int ultima = 0;
    int resposta = 0;

    for (i = 0; i < n; i++) {

        if (consultas[i].inicio >= ultima) {
            resposta++;
            ultima = consultas[i].fim;
        }
        
    }

    printf("%d\n", resposta);

    return 0;
}
