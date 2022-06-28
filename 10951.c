#include <stdio.h>
int main()
{
    int a[10000], b[1024], c = 1, d = 1, n, x = 0, y, i = 0, j, k;

    while (scanf("%d%d", &x, &y) != EOF) {
        printf("%d\n", x + y);
    }
}
