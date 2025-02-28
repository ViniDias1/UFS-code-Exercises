#include <stdio.h>

#define N 8

int board[N][N];
int solution_count = 0;

int is_safe(int row, int col) {
    int i, j;

    // checa a linha
    for (i = 0; i < col; i++)
        if (board[row][i])
            return 0;

    // checa a diagonal superior esquerda
    for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return 0;

    // checa a diagonal inferior esquerda
    for (i = row, j = col; j >= 0 && i < N; i++, j--)
        if (board[i][j])
            return 0;

    // se passar em todas as verificações, a posição é segura
    return 1;
}

void solve(int col) {
    // caso base: todas as rainhas foram colocadas
    if (col >= N) {
        // imprime a solução encontrada
        printf("Solução #%d:\n", solution_count + 1);
        int i, j;
        for (i = 0; i < N; i++) {
            for (j = 0; j < N; j++)
                printf("%d ", board[i][j]);
            printf("\n");
        }
        printf("\n");

        // incrementa o contador de soluções encontradas
        solution_count++;
        return;
    }

    int i;
    for (i = 0; i < N; i++) {
        // checa se a posição (i, col) é segura
        if (is_safe(i, col)) {
            // coloca a rainha na posição (i, col)
            board[i][col] = 1;

            // resolve o problema recursivamente para a próxima coluna
            solve(col + 1);

            // remove a rainha da posição (i, col)
            board[i][col] = 0;
        }
    }
}

int main() {
    // inicializa o tabuleiro com zeros
    int i, j;
    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            board[i][j] = 0;

    // encontra todas as soluções possíveis
    solve(0);

    // imprime o número total de soluções encontradas
    printf("Total de soluções encontradas: %d\n", solution_count);

    return 0;
}

/*
#include <stdio.h>

#define N 8

int board[N][N];

int is_safe(int row, int col) {
    int i, j;

    // checa a linha
    for (i = 0; i < col; i++)
        if (board[row][i])
            return 0;

    // checa a diagonal superior esquerda
    for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return 0;

    // checa a diagonal inferior esquerda
    for (i = row, j = col; j >= 0 && i < N; i++, j--)
        if (board[i][j])
            return 0;

    // se passar em todas as verificações, a posição é segura
    return 1;
}

int solve(int col) {
    // caso base: todas as rainhas foram colocadas
    if (col >= N)
        return 1;

    int i;
    for (i = 0; i < N; i++) {
        // checa se a posição (i, col) é segura
        if (is_safe(i, col)) {
            // coloca a rainha na posição (i, col)
            board[i][col] = 1;

            // resolve o problema recursivamente para a próxima coluna
            if (solve(col + 1))
                return 1;

            // se a solução não for encontrada, remove a rainha da posição (i, col)
            board[i][col] = 0;
        }
    }

    // se nenhuma posição for segura, retorna falso
    return 0;
}

void print_solution() {
    int i, j;
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++)
            printf("%d ", board[i][j]);
        printf("\n");
    }
}

int main() {
    // inicializa o tabuleiro com zeros
    int i, j;
    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            board[i][j] = 0;

    // encontra a solução
    if (solve(0))
        print_solution();
    else
        printf("Não há solução.\n");

    return 0;
}

*/