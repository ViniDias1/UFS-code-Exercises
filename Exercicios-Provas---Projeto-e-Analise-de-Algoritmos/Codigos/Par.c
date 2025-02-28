#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Durante as aulas fui fazendo esbocos do algoritmo para esse problema e busquei adaptar para a questao em contexto.
// Segui a orientacao do livro e customizei algumas coisas por conta propria e apos ver alguns algoritmos ja implementados na internet.
// mesma ideia da questao da montanha. Ja possuia o quick sort implementado, so fiz colocar aqui.

// A solucao com quick sort nao estava passando, por isso que troquei para o mergesort


void mergeBolhas(int vetor[][2], int temp[][2], int meio, int direita, int esquerda,int help) {

    int i = esquerda;
    int j = meio + 1;
    int k = esquerda;

    int contaTroca = 0;
    int aux;
    
    while (i <= meio && j <= direita) {

        if (vetor[i][help] <= vetor[j][help]) {
            temp[k][help] = vetor[i][help];
            k++;
            i++;
        } 
        else {
            temp[k][help] = vetor[j][help];
            k++;
            j++;
            contaTroca += meio - i + 1;
        }
    }
    
    while (i <= meio) {
        temp[k][help] = vetor[i][help];
        k++;
        i++;
    }
    
    while (j <= direita) {
        temp[k][help] = vetor[j][help];
        k++;
        j++;
    }
    
    for (i = esquerda; i <= direita; i++) {
        vetor[i][help] = temp[i][help];
    }
    
}
void mergeSort(int vetor[][2], int temp[][2], int esquerda, int direita, int help) {
    
    if (esquerda < direita) {

        int meio = (esquerda + direita) / 2;

        mergeSort(vetor, temp, esquerda, meio,help);
        mergeSort(vetor, temp, meio + 1, direita,help);
        mergeBolhas(vetor, temp, meio, direita, esquerda,help);
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

    int temp[n][2];
    int help = 0;


    mergeSort(PontosX,temp,0, n-1,help);
    help = 1;
    mergeSort(PontosY,temp,0, n-1,help);
    
    // quickSort(PontosX, 0, n-1);
    // quickSort(PontosY, 0, n-1);

    
 
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

        if (menordistancia >= 10001){
            printf("INFINITY\n");
        }
        else{
            printf("%.4f\n", menordistancia);
        }

        scanf("\n%d",&n);
    }
    
    return 0;

}