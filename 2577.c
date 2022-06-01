#include <stdio.h>
int main()
{
	int x, y, z;
	scanf("%d", &x);
	scanf("%d", &y);
	scanf("%d", &z);
	int k;
	k = x * y * z;
	int i = 0;
	int a[10] = { 0 };

	while (k > 0)
	{
		i = k % 10;
		a[i]++;
		k /= 10;
	}

	for (i = 0; i < 10; i++)
		printf("%d\n", a[i]);
}
