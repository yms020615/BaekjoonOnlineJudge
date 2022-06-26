#include <stdio.h>
int main()
{
    int a[10000], b[1024], c, n, x = 0, y, i, j, k;

    scanf("%d %d", &n, &x);

    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);

    for (i = 0; i < n; i++) {
        if (a[i] < x)
            printf("%d ", a[i]);
    }
}
