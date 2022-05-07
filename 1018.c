#include <stdio.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    int min = 9999, x = 0, y = 0;
    char a[100][100] = {{0, }, };
    for (int i = 0; i < n; i++) {
        scanf("%s", a[i]);
    }
    
    for (int i = 0; i <= n - 8; i++) {
        for (int j = 0; j <= m - 8; j++) {
            x = 0;
            for (int k = 0; k < 8; k++) {
                for (int l = 0; l < 8; l++) {
                    if ((i + j + k + l) % 2 == 0 && a[i + k][j + l] == 'B')
                        x++;
                    else if ((i + j + k + l) % 2 == 1 && a[i + k][j + l] == 'W')
                        x++;
                }
            }
            if (x > 32)
                x = 64 - x;
            if (min > x)
                min = x;
        }
    }
    
    printf("%d", min);
}
