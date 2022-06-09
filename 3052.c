#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int a[10];

	for (int i = 0; i < 10; i++)
		scanf("%d", &a[i]);

	int b[10];
	int k = 1;
	for (int i = 0; i < 10; i++)
	{
		b[i] = a[i] % 42;
	}

	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < i; j++)
		{
			if (b[i] < b[j]) {
				int temp = b[i];
				b[i] = b[j];
				b[j] = temp;
			}
		}
	}

	for (int i = 1; i < 10; i++)
	{
		if (b[i - 1] != b[i])
			k++;
	}

	printf("%d", k);
}
