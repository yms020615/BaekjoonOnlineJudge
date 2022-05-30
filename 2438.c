#include <stdio.h>
int main()
{
    int a[1024], b[1024], c, n, x, y, i, j, k;

    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        for (j = 0; j <= i; j++)
            printf("*");
        printf("\n");
    }
}
