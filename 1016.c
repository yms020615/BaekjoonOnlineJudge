#include <stdio.h>

int notprime[1000001], arr[1000001];

int main() {
    long long min, max, i, j, cnt = 0;
    scanf("%lld %lld", &min, &max);

    for (i = 2; i * i <= max; i++) {
        if (notprime[i] == 1) continue;
        for (j = 2; i * j * i * j <= max; j++) {
            notprime[i * j] = 1;
        }
    }

    for (i = 2; i * i <= max; i++) {
        for (j = min / (i * i); i * i * j <= max; j++) {
            if (i * i * j < min) continue;
            if (notprime[i] == 0) arr[i * i * j - min] = 1;
        }
    }

    for (i = 0; i <= max - min + 1; i++) {
        if (arr[i]) cnt++;
    }

    printf("%lld", max - min + 1 - cnt);

    return 0;
}
