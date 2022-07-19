#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll a[100001], prefix[100001];
ll treeMin[400001], treeMax[400001];

struct node {
	ll all, left, right, ans;
} tree[400001];

ll init1(ll index, ll start, ll end) {
	if (start == end)
		return treeMin[index] = prefix[start];

	ll mid = (start + end) >> 1;
	return treeMin[index] = min(init1(index << 1, start, mid), init1(index << 1 | 1, mid + 1, end));
}

ll query1(ll index, ll start, ll end, ll left, ll right) {
	if (right < start or end < left)
		return 9876543210;

	if (left <= start and end <= right)
		return treeMin[index];

	int mid = (start + end) >> 1;
	return min(query1(index << 1, start, mid, left, right), query1(index << 1 | 1, mid + 1, end, left, right));
}

ll init2(ll index, ll start, ll end) {
	if (start == end)
		return treeMax[index] = prefix[start];

	ll mid = (start + end) >> 1;
	return treeMax[index] = max(init2(index << 1, start, mid), init2(index << 1 | 1, mid + 1, end));
}

ll query2(ll index, ll start, ll end, ll left, ll right) {
	if (right < start or end < left)
		return -9876543210;

	if (left <= start and end <= right)
		return treeMax[index];

	int mid = (start + end) >> 1;
	return max(query2(index << 1, start, mid, left, right), query2(index << 1 | 1, mid + 1, end, left, right));
}

node merge2(node a, node b) {
	node ret;

	ret.all = a.all + b.all;
	ret.ans = max({a.ans, b.ans, a.right + b.left});
	ret.left = max(a.left, a.all + b.left);
	ret.right = max(b.right, b.all + a.right);

	return ret;
}

node init3(ll index, ll start, ll end) {
	if (start == end)
		return tree[index] = {a[start], a[start], a[start], a[start]};

	ll mid = (start + end) >> 1;
	node a = init3(index << 1, start, mid);
	node b = init3(index << 1 | 1, mid + 1, end);
	return tree[index] = merge2(a, b);
}

node query3(ll index, ll start, ll end, ll left, ll right) {
	node ret;

	if (right < start or end < left or right < left)
		return ret = {-9876543210, -9876543210, -9876543210, -9876543210};

	if (left <= start and end <= right)
		return tree[index];

	int mid = (start + end) >> 1;
	return merge2(query3(index << 1, start, mid, left, right), query3(index << 1 | 1, mid + 1, end, left, right));
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		cin >> a[i];
		prefix[i] = prefix[i - 1] + a[i];
	}

	init1(1, 0, n);
	init2(1, 0, n);
	init3(1, 1, n);

	int m;
	ll x1, y1, x2, y2, ans1, ans2, ans3;
	for (cin >> m; m--;) {
		cin >> x1 >> y1 >> x2 >> y2;
		ans1 = query2(1, 0, n, x2, y2) - query1(1, 0, n, x1 - 1, min(y1, x2) - 1);
		ans2 = query2(1, 0, n, max(y1, x2), y2) - query1(1, 0, n, x1 - 1, y1 - 1);
		ans3 = query3(1, 1, n, x2, y1).ans;
		cout << max({ans1, ans2, ans3}) << '\n';
	}
}
