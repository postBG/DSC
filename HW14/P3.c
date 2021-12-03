#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char *input_filename = argv[1]; // name of input file
    char *output_filename = argv[2]; // name of output file

    FILE *input_f = fopen(input_filename, "r");
    FILE *output_f = fopen(output_filename, "w");

    char phone_numbers[20];
    char formatted_numbers[20];
    while (fscanf(input_f, "%s", phone_numbers) != EOF) {
        int len = (int) strlen(phone_numbers);
        int j = 0;
        for(int i = 0; i < len + 1; i ++) {
            if (i == 3 || i == 7) {
                formatted_numbers[j] = '-';
                j++;
            }
            formatted_numbers[j] = phone_numbers[i];
            j++;
        }
        fprintf(output_f, "%s\n", formatted_numbers);
    }

    return 0;
}
