#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

// Nome: VINICIUS DIAS VALEN?A
// Matricula: 202100045850

// esse codigo foi originalmente feito para tentar resolver uma quest?o da disciplina de grafos.

// ao ser passado em uma atividade uma questao chamada "Labirinto para P2", tentei adapta-lo mas tive dificulade
// nas marca??es e desmarca??es dos caminhos percorridos e por isso nao acertei a questao.

// Ja nessa questao, adaptei o codigo para somente percorrer o labirinto com uma abordagem bottom-up.
// se for possivel chegar na posicao [0][0] (marcada como "i"), significa que o labirinto possui saida.


#define tamanhoMAX 1000

char labirinto[tamanhoMAX][tamanhoMAX];
int visitados[tamanhoMAX][tamanhoMAX] = {};
// declarei como variavel global para nao precisar passar como argumento da funcao
int altura,largura;
int stop = 0;
int achou;



void percorrerlabirinto(int linha,int coluna){
	
	if (stop == 1) return;

	if(linha == -1 || coluna == -1 || linha == altura || coluna == largura){
		// limites do labirinto
        return ;
    } 

	if(visitados[linha][coluna] != 0) {
		//vertice marcado
		return ;
    }
	if(labirinto[linha][coluna] == '#') {
		// parede
        return ;
    }
	
	
	if (labirinto[linha][coluna] == 'i'){
		stop =  1;
		// nesse momento, a busca chegou na posicao [0][0]
		achou = 1;
		return;
	}
	

	visitados[linha][coluna] = 1;
	
	// para cima e para baixo
	percorrerlabirinto(linha-1,coluna);
	percorrerlabirinto(linha+1,coluna);
	// lados
	percorrerlabirinto(linha,coluna-1);
	percorrerlabirinto(linha,coluna+1);


	return ;
}


int main(){  

    int i,j;
	scanf("%d %d", &altura,&largura);

	for(i = 0;i < altura ;i++){

		for(j = 0;j < largura;j++){
            scanf(" %c",&labirinto[i][j]);
		}
	}
	
	labirinto[0][0] = 'i';
	int linha = altura - 1,coluna = largura -1;

	
	if(visitados[linha][coluna] == 0){
        percorrerlabirinto(linha,coluna);	
    }
	

	// caso a variavel "achou" tenha sido marcada, basta imprimir YES
	if (achou == 1){
		printf("Yes");
	}
	else{
		printf("No");
	}
	
	return 0;
}