#include <stdio.h>
int main()
{
    int a[10000], b[1024], c = 1, d = 1, n, x = 0, y, i = 0, j, k;

    while (c != 0 || d != 0)
    {
        scanf("%d %d", &c, &d);
        if (c + d == 0)
            break;

        printf("%d\n", c + d);
    }
}
