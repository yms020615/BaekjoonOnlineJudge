#include <bits/stdc++.h>

using namespace std;

int SQRT;
int cnt[1000001];
int a[100001], ans[100001];
int curr;

struct query {
	int left, right, index;
	bool operator<(const query &q) const {
		int x = right / SQRT;
		int y = q.right / SQRT;
		return x == y ? left < q.left : x < y;
	}
} q[100001];

void add_erase(int index, bool add) {
	if (add) {
		if (cnt[a[index]]++ == 0)
			curr++;
	}
	else {
		if (--cnt[a[index]] == 0)
			curr--;
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n;
	cin >> n;
	SQRT = (int)sqrt(n);
	for (int i = 1; i <= n; i++)
		cin >> a[i];

	int m;
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> q[i].left >> q[i].right;
		q[i].index = i;
	}

	sort(q, q + m);

	int low = 1, high = 0;
	for (int i = 0; i < m; i++) {
		while (q[i].left < low)
			add_erase(--low, true);
		while (q[i].left > low)
			add_erase(low++, false);
		while (q[i].right < high)
			add_erase(high--, false);
		while (q[i].right > high)
			add_erase(++high, true);
		ans[q[i].index] = curr;
	}

	for (int i = 0; i < m; i++)
		cout << ans[i] << "\n";
}
