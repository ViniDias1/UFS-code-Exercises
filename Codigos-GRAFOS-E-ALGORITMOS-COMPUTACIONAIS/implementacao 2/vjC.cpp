#include <iostream>
#include <vector>
#include <queue>

// Nome: Vinicius Dias Valenca
// Matricula: 202100045850
 
using namespace std;
 
// codigo feito originalmente em C, mas estava gastando mais tempo implementando a fila de prioridade
// ao inves de resolver o problema em si
int main(){
 
    int vertices, arestas;
 
 
    cin >> vertices >> arestas;
 
    vector<vector<int>> grafo(vertices);
    vector<bool> verticesVisitados(vertices, false);
 
    // fila de prioridade com heap min
    priority_queue<int, vector<int>, greater<int> > fila;
 
    int temp = arestas;
    int lig1,lig2;
 
    while (temp > 0){
        
        cin >> lig1 >> lig2;
        lig1--;lig2--;
        grafo[lig1].push_back(lig2);
        grafo[lig2].push_back(lig1);
 
        // grafo[lig1][vertices]++;
        // grafo[lig2][vertices]++;
 
        temp--;
    }
    
    //int final[vertices];
    //int id = 0;
 
    verticesVisitados[0] = true; 
    fila.push(0);
    int i;
    int vert;
    int atual;
    
    while(!fila.empty()){
 
        atual = fila.top();
        fila.pop();
        //final[id] = atual + 1;
        //Poderia armazernar em um vetor, mas preferi imprimir logo para consumir menos tempo
        cout << atual + 1 << " ";
        //id++;
        
        for (i = 0; i < grafo[atual].size(); i++) {
 
            vert = grafo[atual][i];
            
            if (!verticesVisitados[vert]) {
                fila.push(vert);
                verticesVisitados[vert] = true;
            }
 
        }
    }
    
    return 0;
}