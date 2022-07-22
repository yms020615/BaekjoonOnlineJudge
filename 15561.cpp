#include <bits/stdc++.h>
using namespace std;

const int INF = 1234567890;
int arr[100001];

struct Node {
	int all, left, right, mid;
	Node(int all = 0, int left = -INF, int right = -INF, int mid = -INF)
	: all(all), left(left), right(right), mid(mid) {}
};
Node tree[400001];

Node merge2(Node a, Node b) {
	Node ret;

	ret.all = a.all + b.all;
	ret.left = max(a.left, a.all + b.left);
	ret.right = max(b.right, b.all + a.right);
	ret.mid = max({a.mid, b.mid, a.right + b.left});

	return ret;
}

void update(int node, int start, int end, int index, int val) {
	if (index < start or index > end)
		return;

	if (start == end) {
		tree[node] = Node(val, val, val, val);
		return;
	}

	int mid = (start + end) >> 1;
	update(node << 1, start, mid, index, val);
	update(node << 1 | 1, mid + 1, end, index, val);

	tree[node] = merge2(tree[node << 1], tree[node << 1 | 1]);
}

Node query(int index, int start, int end, int left, int right) {
	if (right < start or end < left)
		return Node();

	if (left <= start and end <= right)
		return tree[index];

	int mid = (start + end) >> 1;
	Node a = query(index << 1, start, mid, left, right);
	Node b = query(index << 1 | 1, mid + 1, end, left, right);

	return merge2(a, b);
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n, q, u, v;
	cin >> n >> q >> u >> v;

	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
		update(1, 1, n, i, u * arr[i] + v);
	}

	int c, a, b;
	while (q--) {
		cin >> c >> a >> b;

		if (c) {
			arr[a] = b;
			update(1, 1, n, a, u * b + v);
		}
		else
			cout << query(1, 1, n, a, b).mid - v << '\n';
	}
}
