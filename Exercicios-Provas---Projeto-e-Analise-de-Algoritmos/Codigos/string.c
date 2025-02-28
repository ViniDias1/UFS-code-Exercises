#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void precompute_shifts(char* pattern, int pattern_size, int* shifts) {
    int i, last_char;
    for (i = 0; i < 256; i++) {
        shifts[i] = pattern_size;
    }
    for (i = 0; i < pattern_size - 1; i++) {
        last_char = (int)pattern[i];
        shifts[last_char] = pattern_size - i - 1;
    }
}

void horspool(char* text, int text_size, char* pattern, int pattern_size) {
    int i, j, last_char, copy_i;
    int shifts[256];
    precompute_shifts(pattern, pattern_size, shifts);
    i = pattern_size - 1;
    char nada = 'F';
    while (i < text_size) {
        j = pattern_size - 1;
        copy_i = i; 
        while (text[copy_i] == pattern[j]) {
            if (j == 0) {
                printf("%d ", i - pattern_size + 1); 
                nada = 'T';
                break;
            }
            copy_i--;
            j--;
        }
        last_char = (int)text[i];
        i += shifts[last_char];
    }
    if(nada == 'F'){
        printf("-1");
    }
    return;
}

int main() {
    char text[2000000];
    char pattern[2000000];
    int text_size, pattern_size, pos;
    scanf("%s", text);
    scanf("%s", pattern);
    text_size = strlen(text);
    pattern_size = strlen(pattern);
    horspool(text, text_size, pattern, pattern_size);
    
    return 0;
}
    
