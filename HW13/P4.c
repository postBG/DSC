#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_LEN 10

void print_unique_numbers(int *numbers, int n_integers);

bool has(int *set, int size, int num);

int main(int argc, char *argv[]) {
    if (argc == 1) {
        printf("Please input at least 1 integer.\n");
    }

    int numbers[MAX_LEN];
    for (int i = 1; i < argc; ++i) {
        int tmp = atoi(argv[i]);
        numbers[i - 1] = tmp;
    }
    print_unique_numbers(numbers, argc - 1);

    return 0;
}

/* Do not modify above*/

bool has(int *set, int size, int num) {
    for (int i = 0; i < size; i++) {
        if (set[i] == num)
            return true;
    }
    return false;
}

void print_unique_numbers(int *numbers, int n_integers) {
    int set[n_integers];
    int size = 0;

    for (int i = 0; i < n_integers; i++) {
        if (!has(set, size, numbers[i])) {
            set[size] = numbers[i];
            size++;
            printf("%d ", numbers[i]);
        }
    }
}