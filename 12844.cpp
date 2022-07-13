#include <bits/stdc++.h>
using namespace std;

int a[500001];
int tree[2000001];
int lazy[2000001];

void init(int index, int start, int end) {
	if (start == end) {
		tree[index] = a[start];
		return;
	}

	int mid = (start + end) >> 1;
	init(index << 1, start, mid);
	init(index << 1 | 1, mid + 1, end);

	tree[index] = tree[index << 1] ^ tree[index << 1 | 1];
}

void propagate(int index, int start, int end) {
	if (lazy[index]) {
		if ((end - start + 1) % 2)
			tree[index] ^= lazy[index];

		if (start ^ end) {
			lazy[index << 1] ^= lazy[index];
			lazy[index << 1 | 1] ^= lazy[index];
		}

		lazy[index] = 0;
	}
}

void update(int index, int start, int end, int val, int left, int right) {
	propagate(index, start, end);

	if (right < start or end < left)
		return;

	if (left <= start and end <= right) {
		lazy[index] ^= val;
		propagate(index, start, end);
		return;
	}

	int mid = (start + end) >> 1;
	update(index << 1, start, mid, val, left, right);
	update(index << 1 | 1, mid + 1, end, val, left, right);

	tree[index] = tree[index << 1] ^ tree[index << 1 | 1];
}

int query(int index, int start, int end, int left, int right) {
	propagate(index, start, end);

	if (right < start or end < left)
		return 0;

	if (left <= start and end <= right)
		return tree[index];

	int mid = (start + end) >> 1;
	int leftQ = query(index << 1, start, mid, left, right);
	int rightQ = query(index << 1 | 1, mid + 1, end, left, right);
	return leftQ ^ rightQ;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n;
	cin >> n;

	for (int i = 1; i <= n; i++)
		cin >> a[i];

	init(1, 1, n);

	int m;
	cin >> m;

	int q1, q2, q3, q4;
	while (m--) {
		cin >> q1;
		if (q1 == 1) {
			cin >> q2 >> q3 >> q4;
			update(1, 1, n, q4, q2 + 1, q3 + 1);
		}
		else {
			cin >> q2 >> q3;
			cout << query(1, 1, n, q2 + 1, q3 + 1) << '\n';
		}
	}
}
