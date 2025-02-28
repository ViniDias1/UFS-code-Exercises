#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int* crivo(int n){
  int A[n+1];
  int i, j, p;
  int nr2 =(int)floor(sqrt((float)n));
  int* L;
  int n_primos = n;//no início todos são primos
  printf("Raiz quadrada (piso) de %d = %d\n", n, nr2);
  
  for(p = 2; p <=n; p++) A[p] = p;
  for(p = 2; p < nr2; p++){
    if(A[p] != 0){
      printf("Removendo os múltiplos de %d\n", p);
      j = p*p;
      while(j <= n){
        if(A[j]){//checa se este número já tinha sido removido da lista
          A[j] = 0;
          printf("%d removido\n", j);
          n_primos--;
        }
      	j = j+p;
      }
      printf("\n");
    }
  }
  L = (int*)malloc(n_primos*sizeof(int));
  //a posição 0 conterá o número de primos na lista.
  L[0] = n_primos-1;
  //A lista de verdade começa na posição 1.
  i = 1; 
  for(p = 2; p <= n; p++)
    if(A[p] != 0)
      L[i++] = A[p];
  return L;
}

int main(){
  int i, n;
  int* primos;
  printf("Digite o n: ");
  scanf("%d", &n);
  printf("Os primos entre 1 e %d são:\n", n);
  primos = crivo(n);
  for(i = 1; i < primos[0]; i++)
    printf("%d, ", primos[i]);
  printf("%d\n", primos[i]);
  return 0;
} 
  
