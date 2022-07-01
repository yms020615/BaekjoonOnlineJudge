#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll a[500001];
ll tree[2000001];
ll lazy[2000001];
ll order[500001];
vector<ll> adj[500001];
int from[500001], to[500001];

int idx = 0;
void dfs(int u) {
	from[u] = ++idx;
	for (ll v : adj[u])
		dfs(v);
	to[u] = idx;
}

void init(int index, int start, int end) {
	if (start == end) {
		tree[index] = order[start];
		return;
	}

	int mid = (start + end) >> 1;
	init(index << 1, start, mid);
	init(index << 1 | 1, mid + 1, end);
}

void propagate(int index, int start, int end) {
	if (lazy[index]) {
		tree[index] += lazy[index];
		if (start ^ end) {
			lazy[index << 1] += lazy[index];
			lazy[index << 1 | 1] += lazy[index];
		}

		lazy[index] = 0;
	}
}

void update(int index, int start, int end, int val, int left, int right) {
	propagate(index, start, end);

	if (right < start or end < left)
		return;

	if (left <= start and end <= right) {
		tree[index] += val;

		if (start ^ end) {
			lazy[index << 1] += val;
			lazy[index << 1 | 1] += val;
		}
		return;
	}

	int mid = (start + end) >> 1;
	update(index << 1, start, mid, val, left, right);
	update(index << 1 | 1, mid + 1, end, val, left, right);
}

ll query(int index, int start, int end, int left, int right) {
	propagate(index, start, end);

	if (right < start or end < left)
		return 0;

	if (left <= start and end <= right)
		return tree[index];

	int mid = (start + end) >> 1;
	ll leftQ = query(index << 1, start, mid, left, right);
	ll rightQ = query(index << 1 | 1, mid + 1, end, left, right);
	return leftQ + rightQ;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n, m;
	cin >> n >> m;
	cin >> a[1];

	int x, y;
	for (int i = 2; i <= n; i++){
		cin >> x >> y;
		a[i] = x;
		adj[y].push_back(i);
	}

	dfs(1);
	for (int i = 1; i <= n; i++)
		order[from[i]] = a[i];
	init(1, 1, n);

	char q1;
	int q2;
	ll q3;
	while (m--) {
		cin >> q1;
		if (q1 == 'p') {
			cin >> q2 >> q3;
			if (from[q2] == to[q2])
				continue;

			update(1, 1, n, q3, from[q2] + 1, to[q2]);
		}
		else {
			cin >> q2;
			cout << query(1, 1, n, from[q2], from[q2]) << '\n';
		}
	}
}
