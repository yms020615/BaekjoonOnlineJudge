#include <stdio.h>

int main() {
    char s[1234567];
    scanf("%[^\n]", s);

    int ans = 0;
    if (s[0] == ' ' && s[1] == '\0') {
        printf("0");
        return 0;
    }

    if (s[0] != ' ' && s[1] == '\0') {
        printf("1");
        return 0;
    }

    for (int i = 1; s[i] != '\0'; i++) {
        if (s[i] == ' ' && s[i+1] != '\0')
            ans++;
    }

    printf("%d", ans + 1);
}
