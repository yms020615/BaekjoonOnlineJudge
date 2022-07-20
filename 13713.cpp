#include <bits/stdc++.h>

using namespace std;

int z[1000001];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	string s;
	cin >> s;
	reverse(s.begin(), s.end());

	int m;
	cin >> m;

	vector<int> query(m);
	for (int i = 0; i < m; i++)
		cin >> query[i];

	int n = s.size();
	z[0] = n;
	for (int i = 1, l = 0, r = 0; i < n; i++) {
		if (i <= r)
			z[i] = min(r - i, z[i - l]);

		while (s[i + z[i]] == s[z[i]])
			z[i]++;

		if (i > r)
			l = i;	

		r = max(r, i + z[i] - 1);
	}

	for (int i = 0; i < m; i++)
		cout << z[n - query[i]] << '\n';
}
