#include <stdio.h>
#include <stdlib.h>

int P4(int n);

int sod(int n) {
    int sum = 0;

    while (n != 0) {
        sum += n % 10;
        n = n / 10;
    }

    return sum;
}

int dr(int n) {
    return 1 + (n - 1) % 9;
}

int dr_star(int n) {
    if (dr(n) % 2 == 0) {
        return dr(n) / 2;
    }
    return (dr(n) + 9) / 2;
}

int abs(int n) {
    if (n < 0)
        return -n;
    return n;
}

int d(int n) {
    if (n == 0)
        return 1;

    int sum = 0;
    while (n != 0) {
        sum += 1;
        n = n / 10;
    }
    return sum;
}

int check(int n) {
    int num_digits = d(n);
    int i;
    for (i = 0; i < num_digits + 1; i++) {
        if (sod(abs(n - dr_star(n) - 9 * i)) == (dr_star(n) + 9 * i)) {
            return 0;
        }
    }
    return 1;
}

int P4(int n) {

    while (1) {
        n = n + 1;
        if (check(n)) {
            return n;
        }
    }
}


// DO NOT MODIFY BELOW!
int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int ans = P4(n);

    printf("%d\n", ans);

    return 0;
}