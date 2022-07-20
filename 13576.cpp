#include <bits/stdc++.h>

using namespace std;

vector<int> Z(string s) {
	int n = s.size();
	vector<int> z(n, 0);
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

	return z;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	string s;
	cin >> s;

	int n = s.length();
	auto z = Z(s);
	auto arr = z;
	sort(arr.begin(), arr.end());

	vector<pair<int, int>> ans;
	for (int i = n; i--;)
		if (i + z[i] == n)
			ans.push_back({z[i], arr.end() - lower_bound(arr.begin(), arr.end(), z[i])});

	cout << ans.size() << '\n';
	for (auto i : ans)
		cout << i.first << ' ' << i.second << '\n';
}
