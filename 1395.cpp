#include <bits/stdc++.h>
using namespace std;

int a[100001];
int tree[400001];
int lazy[400001];

void propagate(int index, int start, int end) {
	tree[index] = (end - start + 1) - tree[index];

	if (start ^ end) {
		lazy[index << 1] ^= 1;
		lazy[index << 1 | 1] ^= 1;
	}

	lazy[index] = 0;
}

void update(int index, int start, int end, int left, int right) {
	if (lazy[index])
		propagate(index, start, end);

	if (right < start or end < left)
		return;

	if (left <= start and end <= right) {
		lazy[index] ^= 1;
		propagate(index, start, end);
		return;
	}

	int mid = (start + end) >> 1;
	update(index << 1, start, mid, left, right);
	update(index << 1 | 1, mid + 1, end, left, right);

	tree[index] = tree[index << 1] + tree[index << 1 | 1];
}

int query(int index, int start, int end, int left, int right) {
	if (lazy[index])
		propagate(index, start, end);

	if (right < start or end < left)
		return 0;

	if (left <= start and end <= right)
		return tree[index];

	int mid = (start + end) >> 1;
	int leftQ = query(index << 1, start, mid, left, right);
	int rightQ = query(index << 1 | 1, mid + 1, end, left, right);
	return leftQ + rightQ;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n, m;
	cin >> n >> m;

	int q1, q2, q3;
	while (m--) {
		cin >> q1 >> q2 >> q3;
		if (q2 > q3)
			swap(q2, q3);

		if (q1 == 0)
			update(1, 1, n, q2, q3);
		else
			cout << query(1, 1, n, q2, q3) << '\n';
	}
}
