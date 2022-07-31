#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll tree[400000];

struct qStruct {
	int t2;
	int t3;
	int t4;
	int count;
};

void update(int node, int left, int right, int index, ll diff) {
	if (index < left || index > right)
		return;

	tree[node] += diff;

	if (left ^ right) {
		int mid = (left + right) >> 1;
		update(node << 1, left, mid, index, diff);
		update(node << 1 | 1, mid + 1, right, index, diff);
	}
}

ll query(int node, int left, int right, int start, int end) {
	if (end < left || right < start)
		return 0;

	if (start <= left && right <= end)
		return tree[node];

	int mid = (left + right) >> 1;

	return query(node << 1, left, mid, start, end) + query(node << 1 | 1, mid + 1, right, start, end);
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

	int m;
	cin >> m;

	vector<pair<int, ll>> q1;
	vector<qStruct> q2;

	int count = 0;
	while (m--) {
		int t1;
		cin >> t1;

		if (t1 == 1) {
			int t2;
			ll t3;
			cin >> t2 >> t3;
			q1.push_back({t2, t3});
		}

		else {
			int t2, t3, t4;
			cin >> t2 >> t3 >> t4;
			q2.push_back({t2, t3, t4, count++});
		}
	}

	sort(q2.begin(), q2.end(), [](qStruct x, qStruct y) {
		return x.t2 < y.t2;
	});

	int k = 0;
	ll ans[100000];
	for (int i = 0; i < q1.size(); i++) {
		while (q2[k].t2 == i) {
			ans[q2[k].count] = query(1, 1, n, q2[k].t3, q2[k].t4);
			k++;
		}
		q1[i].second -= query(1, 1, n, q1[i].first, q1[i].first);
		update(1, 1, n, q1[i].first, q1[i].second);
	}

	for (int i = k; i < q2.size(); i++)
		ans[q2[i].count] = query(1, 1, n, q2[i].t3, q2[i].t4);
	for (int i = 0; i < q2.size(); i++)
		cout << ans[i] << "\n";
}
