#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Linked list node structure */
struct Node {
    int data;
    struct Node *next;
};

/* Create a new node */
struct Node *createNode(struct Node *newNode, int data) {
    newNode = (struct Node *) malloc(sizeof(struct Node));
    newNode->data = data;
    return newNode;
}

int find(struct Node *head, int number) {
    struct Node *curr = head;
    int index = 0;
    while (curr != NULL) {
        if (curr->data == number)
            return index;
        curr = curr->next;
        index++;
    }
    return -1;
}

int list_length(struct Node *head) {
    struct Node *curr = head;
    int len = 0;
    while (curr != NULL) {
        len++;
        curr = curr->next;
    }
    return len;
}

int *get_exists(struct Node *head, int *numbers, int num_numbers) {
    int list_len = list_length(head);
    int *exists = (int *) malloc(sizeof(int) * list_len);
    memset(exists, 0, sizeof(int) * list_len);

    for (int i = 0; i < num_numbers; i++) {
        int index = find(head, numbers[i]);
        if (index == -1)
            continue;
        exists[index] = 1;
    }

    return exists;
}

int count_connected(int *exists, int list_len) {
    int count = 0;
    for (int i = 0; i < list_len; i++) {
        if (exists[i] && (i == 0 || exists[i - 1] == 0)) {
            count++;
            continue;
        }
    }
    return count;
}

int main(int argc, char *argv[]) {
    /* length: the length of input arguments (except for inputList.txt) */
    int length = argc - 2;
    /* inputArr: array of input arguments (except for inputList.txt) */
    int *inputArr = (int *) malloc(sizeof(int) * length);
    /* filepath: path for inputList.txt which will be give as a first argument */
    char *filepath = argv[1];

    /* Create inputArr */
    for (int i = 0; i < length; ++i) {
        inputArr[i] = atoi(argv[i + 2]);
    }

    /* Create a linked list from file input */
    int k = 1;
    struct Node *head = NULL;
    struct Node *prev = NULL;
    struct Node *curr = NULL;

    FILE *fp = fopen(filepath, "r");
    char buffer[10];

    while (fscanf(fp, "%s", buffer) == 1) {
        curr = createNode(curr, atoi(buffer));
        if (k > 1) {
            prev->next = curr;
        } else
            head = curr;

        k++;
        prev = curr;
    }
    curr->next = NULL;
    fclose(fp);

    /* numConnected: the number of connected "cluster" */

    /* Write your code here */
    int *exists = get_exists(head, inputArr, length);
    int numConnected = count_connected(exists, list_length(head));
    /* Do not modify below */
    printf("%d", numConnected);

    free(exists);
    return 0;
}


