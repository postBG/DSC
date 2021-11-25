#include <stdio.h>
#include <stdlib.h>

#define MAX_NUMS 10

void InsertionSortReverse(char list[]);

int main(int argc, char *argv[]) {
    char chars[MAX_NUMS]; //List of characters to be sorted

    if (argc < MAX_NUMS) {
        printf("Please give %d inputs\n", MAX_NUMS);
        return -1;
    }


    for (int index = 0; index < MAX_NUMS; index++) {
        chars[index] = argv[index + 1][0];
    }

    InsertionSortReverse(chars); //Call sorting routine

    //Print sorted list
    for (int index = 0; index < MAX_NUMS; index++)
        printf("%c", chars[index]);

    return 0;
}

void InsertionSortReverse(char list[]) {
    int i, j;
    for(i = 0; i < MAX_NUMS; i++) {
        char max_c = list[i];
        int max_idx = i;
        for(j = i; j < MAX_NUMS; j++) {
            if (max_c < list[j]) {
                max_c = list[j];
                max_idx = j;
            }

        }

        char tmp = list[i];
        list[i] = list[max_idx];
        list[max_idx] = tmp;
    }
}
