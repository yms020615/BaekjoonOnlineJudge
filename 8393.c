#include <stdio.h>
int main()
{
    int a[1024], b[1024], c, n, x = 0, y, i, j, k;

    scanf("%d", &n);

    for (i = 1; i <= n; i++)
        x += i;

    printf("%d", x);
}
