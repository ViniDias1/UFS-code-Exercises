#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct no
{
  char palavra[20];
  struct no *esquerdo, *direito;
  short altura;
} No;

/*
    Função que cria um novo nó
    x -> valor a ser inserido no nó
    Retorna: o endereço do nó criado
*/
No *novoNo(char palavra[20])
{
  No *novo = malloc(sizeof(No));

  if (novo)
  {
    strcpy(novo->palavra, palavra);
    novo->esquerdo = NULL;
    novo->direito = NULL;
    novo->altura = 0;
  }
  else
    printf("\nERRO ao alocar nó em novoNo!\n");
  return novo;
}

/*
    Retorna o maior dentre dois valores
    a, b -> altura de dois nós da árvore
*/
int maior(char a, char b)
{
  return (a > b) ? a : b;
}

//  Retorna a altura de um nó ou -1 caso ele seja null
short alturaDoNo(No *no)
{
  if (no == NULL)
    return -1;
  else
    return no->altura;
}

//   Calcula e retorna o fator de balanceamento de um nó
short fatorDeBalanceamento(No *no)
{
  if (no)
    return (alturaDoNo(no->esquerdo) - alturaDoNo(no->direito));
  else
    return 0;
}

// --------- ROTAÇÕES ---------------------------

// função para a rotação à esquerda
No *rotacaoEsquerda(No *r)
{
  No *y, *f;

  y = r->direito;
  f = y->esquerdo;

  y->esquerdo = r;
  r->direito = f;

  r->altura = maior(alturaDoNo(r->esquerdo), alturaDoNo(r->direito)) + 1;
  y->altura = maior(alturaDoNo(y->esquerdo), alturaDoNo(y->direito)) + 1;

  return y;
}

// função para a rotação à direita
No *rotacaoDireita(No *r)
{
  No *y, *f;

  y = r->esquerdo;
  f = y->direito;

  y->direito = r;
  r->esquerdo = f;

  r->altura = maior(alturaDoNo(r->esquerdo), alturaDoNo(r->direito)) + 1;
  y->altura = maior(alturaDoNo(y->esquerdo), alturaDoNo(y->direito)) + 1;

  return y;
}

No *rotacaoEsquerdaDireita(No *r)
{
  r->esquerdo = rotacaoEsquerda(r->esquerdo);
  return rotacaoDireita(r);
}

No *rotacaoDireitaEsquerda(No *r)
{
  r->direito = rotacaoDireita(r->direito);
  return rotacaoEsquerda(r);
}

/*
    Função para realizar o balanceamento da árvore após uma inserção ou remoção
    Recebe o nó que está desbalanceado e retorna a nova raiz após o balanceamento
*/
No *balancear(No *raiz)
{
  short fb = fatorDeBalanceamento(raiz);

  // Rotação à esquerda
  if (fb < -1 && fatorDeBalanceamento(raiz->direito) <= 0)
    raiz = rotacaoEsquerda(raiz);

  // Rotação à direita
  else if (fb > 1 && fatorDeBalanceamento(raiz->esquerdo) >= 0)
    raiz = rotacaoDireita(raiz);

  // Rotação dupla à esquerda
  else if (fb > 1 && fatorDeBalanceamento(raiz->esquerdo) < 0)
    raiz = rotacaoEsquerdaDireita(raiz);

  // Rotação dupla à direita
  else if (fb < -1 && fatorDeBalanceamento(raiz->direito) > 0)
    raiz = rotacaoDireitaEsquerda(raiz);

  return raiz;
}

/*
    Insere um novo nó na árvore
    raiz -> raiz da árvore
    x -> valor a ser inserido
    Retorno: endereço do novo nó ou nova raiz após o balanceamento
*/
No *inserir(No *raiz, char palavra[20])
{
  if (raiz == NULL) // árvore vazia
    return novoNo(palavra);
  else
  { // inserção será à esquerda ou à direita
    if (strcmp(palavra, raiz->palavra) == -1)
      raiz->esquerdo = inserir(raiz->esquerdo, palavra);
    else if (strcmp(palavra, raiz->palavra) >= 0)
      raiz->direito = inserir(raiz->direito, palavra);
    else
      printf("\nInsercao nao realizada!\nO elemento %s a existe!\n", palavra);
  }

  // Recalcula a altura de todos os nós entre a raiz e o novo nó inserido
  raiz->altura = maior(alturaDoNo(raiz->esquerdo), alturaDoNo(raiz->direito)) + 1;

  // verifica a necessidade de rebalancear a árvore
  raiz = balancear(raiz);

  return raiz;
}

/*
    Função para remover um nó da Árvore binária balanceada
    Pode ser necessário rebalancear a árvore e a raiz pode ser alterada
    por isso precisamos retornar a raiz
*/
No *remover(No *raiz, char chave[20])
{
  if (raiz == NULL)
  {
    printf("Valor nao encontrado!\n");
    return NULL;
  }
  else
  { // procura o nó a remover
    if (strcmp(raiz->palavra, chave) == 0)
    {
      // remove nós folhas (nós sem filhos)
      if (raiz->esquerdo == NULL && raiz->direito == NULL)
      {
        free(raiz);
        printf("Elemento folha removido: %s !\n", chave);
        return NULL;
      }
      else
      {
        // remover nós que possuem 2 filhos
        if (raiz->esquerdo != NULL && raiz->direito != NULL)
        {
          No *aux = raiz->esquerdo;
          while (aux->direito != NULL)
            aux = aux->direito;
          strcpy(raiz->palavra, aux->palavra);
          strcpy(aux->palavra, chave);
          printf("Elemento trocado: %s !\n", chave);
          raiz->esquerdo = remover(raiz->esquerdo, chave);
          return raiz;
        }
        else
        {
          // remover nós que possuem apenas 1 filho
          No *aux;
          if (raiz->esquerdo != NULL)
            aux = raiz->esquerdo;
          else
            aux = raiz->direito;
          free(raiz);
          printf("Elemento com 1 filho removido: %s !\n", chave);
          return aux;
        }
      }
    }
    else
    {
      if (strcmp(chave, raiz->palavra) == -1)
        raiz->esquerdo = remover(raiz->esquerdo, chave);
      else
        raiz->direito = remover(raiz->direito, chave);
    }

    // Recalcula a altura de todos os nós entre a raiz e o novo nó inserido
    raiz->altura = maior(alturaDoNo(raiz->esquerdo), alturaDoNo(raiz->direito)) + 1;

    // verifica a necessidade de rebalancear a árvore
    raiz = balancear(raiz);

    return raiz;
  }
}

void imprimir(No *raiz, int nivel)
{
  int i;
  if (raiz)
  {
    imprimir(raiz->direito, nivel + 1);
    printf("\n\n");

    for (i = 0; i < nivel; i++)
      printf("\t");

    printf("%s", raiz->palavra);
    imprimir(raiz->esquerdo, nivel + 1);
  }
}

int main()
{

  int opcao;
  char valor[20];
  No *raiz = NULL;

  do
  {
    printf("\n\n\t0 - Sair\n\t1 - Inserir\n\t2 - Remover\n\t3 - Imprimir\n\n");
    scanf("%d", &opcao);

    switch (opcao)
    {
    case 0:
      printf("Saindo!!!");
      break;
    case 1:
      printf("\tDigite o valor a ser inserido: ");
      scanf("%s", &valor);
      raiz = inserir(raiz, valor);
      break;
    case 2:
      printf("\tDigite o valor a ser removido: ");
      scanf("%s", &valor);
      raiz = remover(raiz, valor);
      break;
    case 3:
      imprimir(raiz, 1);
      break;
    default:
      printf("\nOpcao invalida!!!\n");
    }

  } while (opcao != 0);

  return 0;
}