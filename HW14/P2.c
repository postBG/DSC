#include <stdio.h>

int main(int argc, char *argv[]) {
    char *input_filename = argv[1]; // name of input file
    FILE *f = fopen(input_filename, "r");
    int num;
    int total = 0;
    while (fscanf(f, "%d", &num) != EOF) {
        total += num;
    }
    printf("%d\n", total);
    return 0;
}
