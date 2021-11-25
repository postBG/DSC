#include <stdio.h>
#include <stdlib.h>

int P1(int n);
// Implement P1
// You can define other function, but P1 must return answer.



int P1(int n) {
    if (n == 0) return 0;

    return 2 * P1(n - 1) + 1;
}


// DO NOT MODIFY BELOW!
int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int ans = P1(n);

    printf("%d\n", ans);

    return 0;
}