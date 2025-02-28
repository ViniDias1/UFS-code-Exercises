#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

// Nome: Vinicius Dias Valenca
// Matricula: 202100045850
 
// igor pode andar pelos "." e so contabiliza se viu o quadro se ele estiver exatemente do lado do "*"
// se baseia em DFS
 
#define tamanhoMAX 1000
 
char museu[tamanhoMAX][tamanhoMAX];
int visitados[tamanhoMAX][tamanhoMAX] = {};
// declarei como variavel global para nao precisar passar como argumento da funcao
int altura,largura;
int regiao;
 
int percorrerMuseu(int linha,int coluna){
 
	if(linha == 0 || coluna == 0 || linha == altura+1 || coluna == largura+1){
		// verifica se as posicoes sao validas
        return 0;
    } 
	if(museu[linha][coluna] == '*') {
        //quadro encontrado
        return 1;
    }
	if(visitados[linha][coluna] != 0) {
		//vertice marcado
		return 0;
    }
	
 
	int quadrosCONT = 0;
	visitados[linha][coluna] = regiao;
 
	//verifica os lados no eixo X
	quadrosCONT += percorrerMuseu(linha+1,coluna);
	quadrosCONT += percorrerMuseu(linha-1,coluna);
	//verifica os lados no eixo Y
	quadrosCONT += percorrerMuseu(linha,coluna+1);
	quadrosCONT += percorrerMuseu(linha,coluna-1);
 
 
	return quadrosCONT;
}
 
 
int main(){  
 
    int i,j,posicao;
	scanf("%d %d %d", &altura,&largura,&posicao);
 
	for(i = 1;i <= altura ;i++){
 
		for(j = 1;j <= largura;j++){
            scanf(" %c",&museu[i][j]);
		}
	}
 
	int linha,coluna;
	int quadros;
	int calculados[posicao];
 
	for(i = 1;i <= posicao;i++){
 
		regiao++;
		scanf("%d %d", &linha,&coluna);
		quadros = 0;	
 
		if(visitados[linha][coluna] == 0){
            quadros = percorrerMuseu(linha,coluna);	
        } 
		else{
			// o "vertice" ja ta marcado, ou seja, o valor dos quadros ja foi calculado.
			// so eh preciso pegar o valor com a em "calculados"
			quadros = calculados[visitados[linha][coluna]];
		}
		calculados[regiao] = quadros;
 
		 
		printf("%d\n",quadros);
		
	}
	return 0;
}