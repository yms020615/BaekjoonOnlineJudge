#include <stdio.h>
int main()
{
    int a[10000], b[1024], c = 1, d = 1, n, x = 0, y, i = 0, j, k;

    scanf("%d", &k);

    y = k;

    do
    {
        x = y / 10 + y % 10;
        y = (y % 10) * 10 + x % 10;
        i++;

    }while (k != y);

    printf("%d", i);
}
