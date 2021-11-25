#include <stdio.h>
#include <stdlib.h>

int P3(int n);

int is_prime(int n) {
    int i;
    for (i = 2; (i * i) <= n; i++) {
        if (n % i == 0)
            return 0;
    }
    return 1;
}

// Implement P3
// You can define other function, but P3 must return answer.
int P3(int n) {
    int sum = 0;
    int i;
    for (i = n; i <= 2 * n; i++) {
        sum += is_prime(i);
    }

    return sum;
}


// DO NOT MODIFY BELOW!
int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int ans = P3(n);

    printf("%d\n", ans);

    return 0;
}