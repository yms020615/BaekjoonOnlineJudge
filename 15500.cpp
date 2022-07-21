#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n;
	cin >> n;

	int temp;
	stack<int> a;
	for (int i = 0; i < n; i++) {
		cin >> temp;
		a.push(temp);
	}

	int curr = n;
	int count = 0;
	vector<pair<int, int>> ans;
	stack<int> b;

	while (curr) {
		while (!a.empty()) {
			if (a.top() < curr) {
				ans.push_back({1, 2});
				b.push(a.top());
			}
			else if (a.top() == curr) {
				ans.push_back({1, 3});
				curr--;
			}

			count++;
			a.pop();
		}

		while (!b.empty()) {
			if (b.top() < curr) {
				ans.push_back({2, 1});
				a.push(b.top());
			}
			else if (b.top() == curr) {
				ans.push_back({2, 3});
				curr--;
			}

			count++;
			b.pop();
		}
	}

	cout << count << '\n';
	for (pair<int, int> i : ans)
		cout << i.first << ' ' << i.second << '\n';
}
