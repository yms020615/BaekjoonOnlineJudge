#include <stdio.h>
int main()
{
    int a[1000000], b[1000000], c, n, x, y, i, j, k;

    scanf("%d", &n);

    for (i = 0; i < n; i++)
        scanf("%d %d", &a[i], &b[i]);

    for (i = 0; i < n; i++)
        printf("%d\n", a[i] + b[i]);
}
