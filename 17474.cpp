#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll arr[1000001];

struct node {
	ll maxVal, subMaxVal, maxCount, sum;
} tree[4000001];

node merge2(node a, node b) {
	if (a.maxVal == b.maxVal)
		return {a.maxVal, max(a.subMaxVal, b.subMaxVal), a.maxCount + b.maxCount, a.sum + b.sum};
	
	if (a.maxVal < b.maxVal)
		swap(a, b);
	
	return {a.maxVal, max(b.maxVal, a.subMaxVal), a.maxCount, a.sum + b.sum};
}

node init(int index, int start, int end) {
	if (start == end)
		return tree[index] = {arr[start], -1, 1, arr[start]};

	int mid = (start + end) >> 1;
	return tree[index] = merge2(init(index << 1, start, mid), init(index << 1 | 1, mid + 1, end));
}

void propagate(int index, int start, int end) {
	if (start == end)
		return;

	for (int i : {index << 1, index << 1 | 1}) {
		if (tree[index].maxVal < tree[i].maxVal) {
			tree[i].sum -= (tree[i].maxVal - tree[index].maxVal) * tree[i].maxCount;
			tree[i].maxVal = tree[index].maxVal;
		}
	}
}

void update(int index, int start, int end, int left, int right, ll val) {
	propagate(index, start, end);

	if (right < start or end < left or tree[index].maxVal <= val)
		return;

	if (left <= start and end <= right and tree[index].subMaxVal <= val) {
		tree[index].sum -= (tree[index].maxVal - val) * tree[index].maxCount;
		tree[index].maxVal = val;
		propagate(index, start, end);
		return;
	}

	int mid = (start + end) >> 1;
	update(index << 1, start, mid, left, right, val);
	update(index << 1 | 1, mid + 1, end, left, right, val);
	tree[index] = merge2(tree[index << 1], tree[index << 1 | 1]);
}

ll query2(int index, int start, int end, int left, int right) {
	propagate(index, start, end);

	if (right < start or end < left)
		return 0;

	if (left <= start and end <= right)
		return tree[index].maxVal;

	int mid = (start + end) >> 1;
	return max(query2(index << 1, start, mid, left, right), query2(index << 1 | 1, mid + 1, end, left, right));
}

ll query3(int index, int start, int end, int left, int right) {
	propagate(index, start, end);

	if (right < start or end < left)
		return 0;

	if (left <= start and end <= right)
		return tree[index].sum;

	int mid = (start + end) >> 1;
	return query3(index << 1, start, mid, left, right) + query3(index << 1 | 1, mid + 1, end, left, right);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;

	for (int i = 1; i <= n; i++)
		cin >> arr[i];

	init(1, 1, n);

	int m;
	int q1, q2, q3;
	ll q4;
	for (cin >> m; m--;) {
		cin >> q1 >> q2 >> q3;
		if (q1 == 1) {
			cin >> q4;
			update(1, 1, n, q2, q3, q4);
		}
		else if (q1 == 2)
			cout << query2(1, 1, n, q2, q3) << '\n';
		else
			cout << query3(1, 1, n, q2, q3) << '\n';
	}
}
