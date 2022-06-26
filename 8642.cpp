#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int SQRT;
ll cnt[1000001];
ll a[100001], ans[100001];

struct query {
	int left, right, index;
	bool operator<(const query &q) const {
		int x = right / SQRT;
		int y = q.right / SQRT;
		return x == y ? left < q.left : x < y;
	}
} q[100001];

ll sum = 0;
void add_erase(int index, bool add) {
	if (add) {
		sum -= cnt[a[index]] * cnt[a[index]] * a[index];
		cnt[a[index]]++;
		sum += cnt[a[index]] * cnt[a[index]] * a[index];
	}
	else {
		sum -= cnt[a[index]] * cnt[a[index]] * a[index];
		cnt[a[index]]--;
		sum += cnt[a[index]] * cnt[a[index]] * a[index];
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n, m;
	cin >> n >> m;

	SQRT = (int)sqrt(n);
	for (int i = 1; i <= n; i++)
		cin >> a[i];

	for (int i = 0; i < m; i++) {
		cin >> q[i].left >> q[i].right;
		q[i].index = i;
	}

	sort(q, q + m);

	int low = q[0].left, high = q[0].right;
	for (int i = low; i <= high; i++)
		add_erase(i, true);
	ans[q[0].index] = sum;

	for (int i = 1; i < m; i++) {
		while (q[i].left < low)
			add_erase(--low, true);
		while (q[i].left > low)
			add_erase(low++, false);
		while (q[i].right < high)
			add_erase(high--, false);
		while (q[i].right > high)
			add_erase(++high, true);
		ans[q[i].index] = sum;
	}

	for (int i = 0; i < m; i++)
		cout << ans[i] << "\n";
}
