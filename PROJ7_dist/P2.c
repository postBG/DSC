#include <stdio.h>
#include <stdlib.h>

// A structure to represent a stack
struct Stack {
    int top;
    unsigned capacity;
    char *array;
};

// function to create a stack of given capacity. It initializes size of
// stack as 0
struct Stack *createStack(unsigned capacity) {
    struct Stack *stack = (struct Stack *) malloc(sizeof(struct Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (char *) malloc(stack->capacity * sizeof(char));
    return stack;
}

// Stack is full when top is equal to the last index
int isFull(struct Stack *stack) {
    return stack->top == stack->capacity - 1;
}

// Stack is empty when top is equal to -1
int isEmpty(struct Stack *stack) {
    return stack->top == -1;
}

// Function to add an item to stack.  It increases top by 1
void push(struct Stack *stack, char item) {
    if (isFull(stack))
        return;
    stack->array[++stack->top] = item;
}

// Function to remove an item from stack.  It decreases top by 1
char pop(struct Stack *stack) {
    if (isEmpty(stack))
        return '0';
    return stack->array[stack->top--];
}

int len(char *s) {
    int l = 0;
    while (s[l] != '\0') {
        l += 1;
    }
    return l;
}

int is_success(struct Stack *stack, char *str) {
    int l = len(str);

    for (int i = 0; i < l; i++) {
        char c = str[i];

        if (c == '(' || c == '{' || c == '[') {
            push(stack, c);
            continue;
        }

        if (c == ')' && pop(stack) != '(')
            return -1;

        if (c == '}' && pop(stack) != '{')
            return -1;

        if (c == ']' && pop(stack) != '[')
            return -1;
    }

    return isEmpty(stack) - 1;
}

int main(int argc, char *argv[]) {

    char *strInput = argv[1];
    int success = 0; // 0 on success, -1 on failure

    /* Write your code here */

    struct Stack *stack = createStack(len(strInput));
    success = is_success(stack, strInput);

    /* Do not modify below */
    printf("%d", success);

    return 0;


}


