#include <stdio.h>
#include <stdlib.h>

#define MAX_LEN 10

char *SwitchCase(char *s);

int len(char *s) {
    int l = 0;
    while (s[l] != '\0') {
        l += 1;
    }
    return l;
}

char *SwitchCase(char *s) {
    int l = len(s);
    int i;
    for (i = 0; i < l; i++) {
        char c = s[i];
        if ('a' <= c && c <= 'z')
            s[i] = c - 32;
        else
            s[i] = c + 32;
    }
    return s;
}

int main(int argc, char *argv[]) {
    char *str; //List of characters to be sorted

    str = argv[1];
    printf("%s", SwitchCase(str));

    return 0;
}
