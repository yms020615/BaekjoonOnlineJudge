#include <bits/stdc++.h>

using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n;
	cin >> n;

	long long a[91];
	a[0] = 0;
	a[1] = 1;

	for (int i = 2; i <= n; i++)
		a[i] = a[i - 1] + a[i - 2];

	cout << a[n];
}
