#include <stdio.h>

int factorization(int num, int *prime_numbers) {
    int j = 0;
    int i = 2;
    while (num != 1) {
        while (num % i == 0) {
            prime_numbers[j++] = i;
            num /= i;
        }
        i++;
    }

    return j;
}

void print_prime_numbers(int num, int *prime_numbers, int num_primes, FILE *output_f) {
    fprintf(output_f, "%d = ", num);

    for (int i = 0; i < num_primes - 1; i++) {
        fprintf(output_f, "%d * ", prime_numbers[i]);
    }
    fprintf(output_f, "%d\n", prime_numbers[num_primes - 1]);
}

int main(int argc, char *argv[]) {
    char *input_filename = argv[1]; // name of input file
    char *output_filename = argv[2]; // name of output file

    FILE *input_f = fopen(input_filename, "r");
    FILE *output_f = fopen(output_filename, "w");

    int prime_numbers[65];
    int num;
    while (fscanf(input_f, "%d", &num) != EOF) {
        int num_primes = factorization(num, prime_numbers);
        print_prime_numbers(num, prime_numbers, num_primes, output_f);
    }

    return 0;
}
