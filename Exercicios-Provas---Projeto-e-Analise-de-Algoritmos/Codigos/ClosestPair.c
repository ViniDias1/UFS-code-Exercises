#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Durante as aulas fui fazendo esbocos do algoritmo para esse problema e busquei adaptar para a questao em contexto.
// Segui a orientacao do livro e customizei algumas coisas por conta propria e apos ver alguns algoritmos ja implementados na internet.
// mesma ideia da questao da montanha. Ja possuia o quick sort implementado, so fiz colocar aqui.


int particao(int vet[][2], int inicio, int fim){
	int pivo, indicePivo, i;
	
	pivo = vet[fim][0]; 
	indicePivo = inicio;
	
	for(i = inicio; i < fim; i++){
		
		if(vet[i][0] <= pivo){
            int aux1 = vet[i][0];
            int aux2 = vet[i][1];

            vet[i][0] = vet[indicePivo][0];
            vet[indicePivo][0] = aux1;

            vet[i][1] = vet[indicePivo][1];
            vet[indicePivo][1] = aux2;

			indicePivo++;
		}
	}

    int aux1 = vet[indicePivo][0];
    int aux2 = vet[indicePivo][1];

	vet[indicePivo][0] = vet[fim][0];
	vet[fim][0] = aux1;

    vet[indicePivo][1] = vet[fim][1];
    vet[fim][1] = aux2;

	
	return indicePivo;
}


int particicaoRandom(int vet[][2], int inicio, int fim){

	int indicePivo = (rand() % (fim - inicio + 1)) + inicio;
    
    int aux1 = vet[indicePivo][0];
    int aux2 = vet[indicePivo][1];

	vet[indicePivo][0] = vet[fim][0];
	vet[fim][0] = aux1;

    vet[indicePivo][1] = vet[fim][1];
    vet[fim][1] = aux2;
	
	return particao(vet, inicio, fim);
}

void quickSort(int vet[][2], int inicio, int fim){

	if(inicio < fim){
		
		int indicePivo = particicaoRandom(vet, inicio, fim);
	
		quickSort(vet, inicio, indicePivo - 1);
		quickSort(vet, indicePivo + 1, fim);
	}
}


float distancia(int p1[], int p2[]){
    return sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]));
}



float forcaBruta(int P[][2], int n)
{
    float min = 999999.9999;
    float temp;
    for (int i = 0; i < n; ++i){

        for (int j = i+1; j < n; ++j){
            temp = distancia(P[i], P[j]);
            if (temp < min){
                min = temp;
            }
        }
            
    }
    
    return min;
}



float maisPertoSUB(int parte[][2], int tamanho, float distanciaTEMP)
{
    float min = distanciaTEMP;
    float temp;
    int i,j;

    for (i = 0; i < tamanho; ++i){
        for (j = i+1; j < tamanho && (parte[j][1] - parte[i][1]) < min; ++j){

            temp = distancia(parte[i],parte[j]);
            if (temp < min){
                min = temp;
            }
        }
    }
             
    return min;
}


float maisPertoPRINCIPAL(int PontosX[][2], int PontosY[][2], int n){
	
	if (n <= 3){
        return forcaBruta(PontosX, n);
    }
		
	int indiceMeio = n/2;
	int PontoMEIO[2];
	PontoMEIO[0] = PontosX[indiceMeio][0];
	PontoMEIO[1] = PontosX[indiceMeio][1];

	
	int PontosYEsq[indiceMeio][2]; 
	int PontosYDir[n-indiceMeio][2]; 

	int indiceEsq = 0, indiceDir = 0; 
	for (int i = 0; i < n; i++)
	{
		if ((PontosY[i][0] < PontoMEIO[0] || (PontosY[i][0] == PontoMEIO[0] && PontosY[i][1] < PontoMEIO[1])) && indiceEsq<indiceMeio)
		{
			PontosYEsq[indiceEsq][0] = PontosY[i][0];
			PontosYEsq[indiceEsq][1] = PontosY[i][1];
			indiceEsq++;
		}
		else
		{
			PontosYDir[indiceDir][0] = PontosY[i][0];
			PontosYDir[indiceDir][1] = PontosY[i][1];
			indiceDir++;
		}
	}

	
	float lineEsq = maisPertoPRINCIPAL(PontosX, PontosYEsq, indiceMeio);
	float lineDir = maisPertoPRINCIPAL(PontosX + indiceMeio, PontosYDir, n-indiceMeio);

	
	float distanciaTEMP;
    if (lineEsq < lineDir) {
        distanciaTEMP = lineEsq;
    } else {
        distanciaTEMP = lineDir;
    }


	int parte[n][2];
	int j = 0;
	for (int i = 0; i < n; i++){
        if (abs(PontosY[i][0] - PontoMEIO[0]) < distanciaTEMP){
			parte[j][0] = PontosY[i][0];
			parte[j][1] = PontosY[i][1];
			j++;
		}
    }

	return maisPertoSUB(parte, j, distanciaTEMP);
}


float maisPertoINICIO(int vet[][2], int n){

    int PontosX[n][2];
    int PontosY[n][2];

    for (int i = 0; i < n; i++){
        PontosX[i][0] = vet[i][0];
        PontosX[i][1] = vet[i][1];
        PontosY[i][0] = vet[i][0];
        PontosY[i][1] = vet[i][1];

    }
    
    quickSort(PontosX, 0, n-1);
    quickSort(PontosY, 0, n-1);
 
    return maisPertoPRINCIPAL(PontosX, PontosY, n);
}

int main(){

    int n,i;
    
    scanf("%d",&n);
    
    while (n != 0){

        int coordenadas[n][2];
        int i;
        for (i = 0; i < n; i++) {
            scanf("%d%d", &coordenadas [i][0], &coordenadas [i][1]);
        }

        float menordistancia = maisPertoINICIO(coordenadas,n);

        if (menordistancia >= 10000.0000){
            printf("INFINITY\n");
        }
        else{
            printf("%.4f\n", menordistancia);
        }

        scanf("\n%d",&n);
    }
    
    return 0;

}