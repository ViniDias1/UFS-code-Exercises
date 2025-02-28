#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>

typedef struct {
	int n;
	int* elements;
} t_vector;

t_vector repetidas(t_vector album, t_vector novas){
int indiceAlbum = 0;
    int indiceNovas = 0;
    int indiceVetorFinal = 0;

    t_vector vetorFinal;
    vetorFinal.elements = (int*)malloc((album.n + novas.n)*sizeof(int));
    vetorFinal.n = 0;

    while (indiceAlbum < album.n && indiceNovas < novas.n){
        // se o numero for igual, ambos os indices dos vetores dados � incrementado
        // o tamanho do vetor de repetidas aumenta
        // o indice do vetorFinal so aumenta quando uma repeti�ao acontece
        if (album.elements[indiceAlbum] == novas.elements[indiceNovas]){
            vetorFinal.elements[indiceVetorFinal] = album.elements[indiceAlbum];
            vetorFinal.n++;
            indiceAlbum++;
            indiceNovas++;
            indiceVetorFinal++;
        }
        else{
            // como sao vetores ordenados, nao � necessario comparar valores novamente, ja que os valores sao podem estar em um 
            // intervalo ate um numero <= a ele.
            if (album.elements[indiceAlbum] < novas.elements[indiceNovas]){
                indiceAlbum++;
            }
            else{
                indiceNovas++;  
            }
        }
    }

    return vetorFinal;
} 

int main() {
	int i, j, k;
	t_vector album, novas, reps;
	scanf("%d", &album.n);
	album.elements = (int*)malloc((album.n+1)*sizeof(int));
	for(i = 0; i < album.n; i++){
		scanf("%d", &(album.elements[i]));
	}
	album.elements[i] = INT_MAX;
	
	scanf("%d", &novas.n);
	novas.elements = (int*)malloc((novas.n+1)*sizeof(int));
	for(i = 0; i < novas.n; i++){
		scanf("%d", &(novas.elements[i]));
	}
	novas.elements[i] = INT_MAX;
	
	reps = repetidas(album, novas);
	
	for(k = 0; k < reps.n-1; k++)
	  printf("%d ", reps.elements[k]);
	printf("%d\n", reps.elements[k]);
	
	free(reps.elements);
	free(album.elements);
	free(novas.elements);
	
	return 0;
}
