#include <stdio.h>
int main()
{
    int a[1024], b[1024], c, n, x = 0, y, i, j, k;

    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            printf(" ");
        }

        for (k = 0; k <= i; k++)
            printf("*");

        printf("\n");
    }
}
