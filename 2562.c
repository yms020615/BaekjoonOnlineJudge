#include <stdio.h>
int main()
{
    int a[100], b[1024], c = 1, d = 1, n, x = 0, y, i = 0, j, k;

    n = 9;

    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);

    y = a[0];
    k = 0;

    for (i = 0; i < n; i++)
    {
        if (y < a[i])
        {
            y = a[i];
            k = i;
        }
    }

    printf("%d\n%d", y, k + 1);
}
