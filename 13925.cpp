#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll a[100001];
ll tree[400001];
ll lazy1[400001];
ll lazy2[400001];
const ll MOD = 1000000007;

void init(int index, int start, int end) {
	if (start == end) {
		tree[index] = a[start];
		return;
	}

	int mid = (start + end) >> 1;
	init(index << 1, start, mid);
	init(index << 1 | 1, mid + 1, end);

	tree[index] = (tree[index << 1] + tree[index << 1 | 1]) % MOD;
}

void propagate(int index, int start, int end) {
	if (lazy1[index] != 1 or lazy2[index] != 0) {
		tree[index] = (tree[index] * lazy1[index] + ((ll)end - start + 1) * lazy2[index]) % MOD;

		if (start ^ end) {
			lazy1[index << 1] *= lazy1[index];
			lazy1[index << 1] %= MOD;

			lazy1[index << 1 | 1] *= lazy1[index];
			lazy1[index << 1 | 1] %= MOD;

			lazy2[index << 1] *= lazy1[index];
			lazy2[index << 1] %= MOD;
			lazy2[index << 1] += lazy2[index];
			lazy2[index << 1] %= MOD;

			lazy2[index << 1 | 1] *= lazy1[index];
			lazy2[index << 1 | 1] %= MOD;
			lazy2[index << 1 | 1] += lazy2[index];
			lazy2[index << 1 | 1] %= MOD;
		}

		lazy1[index] = 1;
		lazy2[index] = 0;
	}
}

void update(int index, int start, int end, ll val, int left, int right, int order) {
	propagate(index, start, end);

	if (right < start or end < left)
		return;

	if (left <= start and end <= right) {
		if (order == 1) {
			lazy1[index] = 1;
			lazy2[index] = val;
		}
		else if (order == 2) {
			lazy1[index] = val;
			lazy2[index] = 0;
		}
		else {
			lazy1[index] = 0;
			lazy2[index] = val;
		}

		propagate(index, start, end);
		return;
	}

	int mid = (start + end) >> 1;
	update(index << 1, start, mid, val, left, right, order);
	update(index << 1 | 1, mid + 1, end, val, left, right, order);

	tree[index] = (tree[index << 1] + tree[index << 1 | 1]) % MOD;
}

int query(int index, int start, int end, int left, int right) {
	propagate(index, start, end);

	if (right < start or end < left)
		return 0;

	if (left <= start and end <= right)
		return tree[index];

	int mid = (start + end) >> 1;
	int leftQ = query(index << 1, start, mid, left, right) % MOD;
	int rightQ = query(index << 1 | 1, mid + 1, end, left, right) % MOD;
	return (leftQ + rightQ) % MOD;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n;
	cin >> n;

	for (int i = 1; i <= n; i++)
		cin >> a[i];

	fill(tree, tree + 4 * n, 0);
	fill(lazy1, lazy1 + 4 * n, 1);
	fill(lazy2, lazy2 + 4 * n, 0);
	init(1, 1, n);

	int m;
	cin >> m;

	int q1, q2, q3;
	ll q4;
	while (m--) {
		cin >> q1;
		if (q1 == 1 or q1 == 2 or q1 == 3) {
			cin >> q2 >> q3 >> q4;
			update(1, 1, n, q4, q2, q3, q1);
		}
		else {
			cin >> q2 >> q3;
			cout << query(1, 1, n, q2, q3) % MOD << '\n';
		}
	}
}
