#include <bits/stdc++.h>

using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n;
	cin >> n;

	int grundy = 0;
	for (int i = 0; i < n; i++) {
		int p;
		cin >> p;
		grundy ^= p;
	}

	if (grundy)
		cout << "koosaga";
	else
		cout << "cubelover";
}
