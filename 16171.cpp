#include <bits/stdc++.h>

using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	string s, k;
	cin >> s;
	cin >> k;

	string s2;
	for (int i = 0; i < s.length(); i++)
		if (!('0' <= s[i] && s[i] <= '9'))
			s2 += s[i];

	bool flag;
	int len_k = k.length();
	for (int i = len_k; i <= s.length(); i++) {
		flag = true;
		for (int j = len_k; j > 0; j--) {
			if (s2[i - j] != k[len_k - j]) {
				flag = false;
				break;
			}
		}
		if (flag)
			break;
	}

	cout << flag ? 1 : 0;
}
