#include <iostream>
#include <vector>

// Nome: Vinicius Dias Valenca
// Matricula: 202100045850

using namespace std;
// ao declarar o tamanho como 5000, o erro de STATUS_ACCESS_VIOLATION estava ocorrendo
// por isso aumentei a margem em 10 para previnir esse erro

int visitados[5010] = {};
vector<int> grafo[5010];

// a partir da capital irei percorrer todos os vertices que sao posseveis chegar atraves dela
// depois farei a mesmo coisa com os vertices que nao foram alcancados da primeira vez.


void buscaProfundidade(int inicio, int origem){

    // cada vertice sera marcado com o numero da cidade que deu origem a busca

    if (visitados[inicio] != origem){

        visitados[inicio] = origem;
    

        for (int prox : grafo[inicio]){
            buscaProfundidade(prox,origem);
        }
    }
    return;

}

int main(){
    int numeroCidades, estradas, capital;
    
    cin>>numeroCidades>>estradas>>capital;

    //esse eh um jeito de declarar uma matriz com vetores internos de tamanho nao definido

    int i;
    int lig1,lig2;

    for ( i = 0; i < estradas; i++){
        
        cin>>lig1>>lig2;
        grafo[lig1].push_back(lig2);

    }

    if (estradas == 0){
        
        cout<<numeroCidades - 1;
    }
    else{

        buscaProfundidade(capital,capital);
        
        // percorre os vertices nao alcancados anteriormente
        for (i = 1; i <= numeroCidades; i++){
            
            if (visitados[i] == 0 ){
                buscaProfundidade(i,i);
            }
        }

        int verificador[numeroCidades + 1] = {};
        int cont = 0;
        int verificar;
        
        for (i = 1; i <= numeroCidades; i++){
            
            verificar = visitados[i];
            // percorre os vertices visistados a partir do indice armazenado em visitados[]
            if (verificador[verificar] == 0){
                
                verificador[verificar] = 1;
                cont++;
            }
        }
        
        // caso a capital esta "isolada" sera diminuido 1 para concertar a contagem 

        cout << cont - verificador[capital] << endl;
    }

        

    
    return 0;
}

