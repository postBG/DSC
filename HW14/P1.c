#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int N = atoi(argv[1]);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N - i - 1; j++) {
            printf(" ");
        }
        for (int j = 0; j < 2 * i + 1; j++) {
            printf("*");
        }

        printf("\n");
    }
    return 0;
}