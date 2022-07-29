#include <bits/stdc++.h>

using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n;
	cin >> n;

	vector<int> p;
	for (int i = 0; i < n; i++) {
		int temp;
		cin >> temp;
		p.push_back(temp);
	}

	int ans = 0;
	for (int i = 0; i < n; i++) {
		int grundy = 0;

		for (int j = 0; j < n; j++) {
			if (j == i)
				continue;
			grundy ^= p[j];
		}

		for (int j = 0; j < p[i]; j++)
			if (!(grundy ^ j))
				ans++;
	}

	cout << ans;
}
