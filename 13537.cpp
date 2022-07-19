#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

vector<ll> tree[400001];

void update(int node, int left, int right, int index, ll k) {
	if (index < left || index > right)
		return;

	tree[node].push_back(k);

	int mid = (left + right) / 2;

	if (left != right) {
		update(node * 2, left, mid, index, k);
		update(node * 2 + 1, mid + 1, right, index, k);
	}
}

int query(int node, ll k, int start, int end, int left, int right) {
	if (end < left || right < start)
		return 0;

	if (start <= left && right <= end)
		return tree[node].end() - upper_bound(tree[node].begin(), tree[node].end(), k);

	int mid = (left + right) / 2;

	return query(node * 2, k, start, end, left, mid) + query(node * 2 + 1, k, start, end, mid + 1, right);
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n;
	cin >> n;

	int temp;
	for (int i = 1; i <= n; i++) {
		cin >> temp;
		update(1, 1, n, i, temp);
	}

	for (int i = 0; i <= 4 * n; i++)
		sort(tree[i].begin(), tree[i].end());

	int m;
	cin >> m;

	int x, y;
	ll z;
	while (m--) {
		cin >> x >> y >> z;
		cout << query(1, z, x, y, 1, n) << "\n";
	}
}
