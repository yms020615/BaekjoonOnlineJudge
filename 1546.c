#include <stdio.h>
int main()
{
	int n;
	float a[1000] = { 0 };
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);

	for (int i = 0; i < n; i++)
		for (int j = 0; j < i; j++)
		{
			if (a[i] < a[j])
			{
				float temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		}

	float sum = 0;

	for (int i = 0; i < n; i++)
	{
		a[i] = a[i] / a[n - 1] * 100;
		sum += a[i];
	}

	printf("%f", sum / n);
}
