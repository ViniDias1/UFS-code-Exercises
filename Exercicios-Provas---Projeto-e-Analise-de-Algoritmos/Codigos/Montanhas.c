#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Nome: Vinicius Dias Valenca
// Matricula: 202100045850

// o quickSort ja tinha sido implementado por mim durante as aulas.
// So fiz adptar para lidar com a situacao problema
// usei a ideia de escolher um pivo de forma aleatoria

void troca(int vet[][2], int i, int j){
	int aux1 = vet[i][0];
    int aux2 = vet[i][1];

	vet[i][0] = vet[j][0];
	vet[j][0] = aux1;

    vet[i][1] = vet[j][1];
    vet[j][1] = aux2;

}


int particao(int vet[][2], int inicio, int fim){
	int pivo, indicePivo, i;
	
	pivo = vet[fim][0]; 
	indicePivo = inicio;
	
	for(i = inicio; i < fim; i++){
		
		if(vet[i][0] <= pivo){

			troca(vet, i, indicePivo);
			indicePivo++;
		}
	}

	troca(vet, indicePivo, fim);
	
	return indicePivo;
}


int particicaoRandom(int vet[][2], int inicio, int fim){

	int indicePivo = (rand() % (fim - inicio + 1)) + inicio;
	
	troca(vet, indicePivo, fim);
	
	return particao(vet, inicio, fim);
}

void quickSort(int vet[][2], int inicio, int fim){

	if(inicio < fim){
		
		int indicePivo = particicaoRandom(vet, inicio, fim);
	
		quickSort(vet, inicio, indicePivo - 1);
		quickSort(vet, indicePivo + 1, fim);
	}
}


float tamanhoLinhas(int n, int coordenadas [][2]) {
    float tamanho = 0;
    float maxY = 0;
    
    for (int i = n - 2; i >= 0; i--) {

        //ponto mais a esquerda
        int x1 = coordenadas [i][0];
        int y1 = coordenadas [i][1];
        
        //ponto mais a direita
        int x2 = coordenadas [i+1][0];
        int y2 = coordenadas [i+1][1];

        if (y1 >= maxY) {
            
            float inclinacao = (float) (y1 - y2) / (x1 - x2);
            float x = x1 - (y1 - maxY) / inclinacao;

            float catetoY = y1 - maxY;
            float catetoX = x - x1;

            float linhaDaVez = sqrt(catetoX*catetoX + catetoY*catetoY);
            tamanho += linhaDaVez;

            maxY = y1;
        } 
    }
    return tamanho;
}

int main() {

    int t;
    scanf("%d", &t);

    while (t--) {

        int n;
        scanf("%d", &n);

        int coordenadas [n][2];

        for (int i = 0; i < n; i++) {
            scanf("%d%d", &coordenadas [i][0], &coordenadas [i][1]);
        }
        
        
        quickSort(coordenadas, 0, n - 1);

        float tamanho = tamanhoLinhas(n, coordenadas) * 1.00000;
        printf("%.2f\n", tamanho);
    }
    return 0;
}
