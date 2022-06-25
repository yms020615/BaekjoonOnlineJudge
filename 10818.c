#include <stdio.h>
int main()
{
    int a[1000000], b[1024], c = 1, d = 1, n, x = 0, y, i = 0, j, k;

    scanf("%d", &n);

    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);

    x = a[0];
    y = a[0];

    for (i = 0; i < n; i++)
    {
        if (x > a[i]) x = a[i];
        if (y < a[i]) y = a[i];
    }

    printf("%d %d", x, y);
}
