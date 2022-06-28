#include <bits/stdc++.h>

using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n;
	cin >> n;

	int a[10001], temp;
	fill_n(a, 10001, 0);
	
	for (int i = 0; i < n; i++) {
		cin >> temp;
		a[temp]++;
	}

	for (int i = 1; i <= 10000; i++)
		while (a[i]--)
			cout << i << '\n';
}
