#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
ll a[100001];
ll tree[400001];
ll lazy[400001];

void propagate(ll index, ll start, ll end) {
	if (lazy[index]) {
		tree[index] += (end - start + 1) * lazy[index];

		if (start ^ end) {
			lazy[index << 1] += lazy[index];
			lazy[index << 1 | 1] += lazy[index];
		}

		lazy[index] = 0;
	}
}

void update(ll index, ll start, ll end, ll val, ll left, ll right) {
	propagate(index, start, end);

	if (right < start or end < left)
		return;

	if (left <= start and end <= right) {
		tree[index] += (end - start + 1) * (ll)val;

		if (start ^ end) {
			lazy[index << 1] += val;
			lazy[index << 1 | 1] += val;
		}

		propagate(index, start, end);
		return;
	}

	ll mid = (start + end) >> 1;
	update(index << 1, start, mid, val, left, right);
	update(index << 1 | 1, mid + 1, end, val, left, right);

	tree[index] = tree[index << 1] + tree[index << 1 | 1];
}

ll query(ll index, ll start, ll end, ll left, ll right) {
	propagate(index, start, end);

	if (right < start or end < left)
		return 0;

	if (left <= start and end <= right)
		return tree[index];

	ll mid = (start + end) >> 1;
	ll leftQ = query(index << 1, start, mid, left, right);
	ll rightQ = query(index << 1 | 1, mid + 1, end, left, right);
	return leftQ + rightQ;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	ll n;
	cin >> n;

	for (ll i = 1; i <= n; i++)
		cin >> a[i];

	for (ll i = 1; i <= n; i++)
		update(1, 1, n, a[i] - a[i - 1], i, i);

	ll m;
	cin >> m;

	ll q1, q2, q3;
	while (m--) {
		cin >> q1;
		if (q1 == 1) {
			cin >> q2 >> q3;
			update(1, 1, n, 1, q2, q3);
			update(1, 1, n, -(q3 - q2 + 1), q3 + 1, q3 + 1);
		}
		else {
			cin >> q2;
			cout << query(1, 1, n, 1, q2) << '\n';
		}
	}
}
