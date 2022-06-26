#include <bits/stdc++.h>

using namespace std;

int SQRT;
int cnt[10001], ans[10001];
int a[300001];
int curr;

struct query {
	int left, right, index;
	bool operator<(const query &q) const {
		int x = right / SQRT;
		int y = q.right / SQRT;
		return x == y ? left < q.left : x < y;
	}
} q[100001];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n, c;
	cin >> n >> c;
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
			cnt[a[--low]]++;
		while (q[i].left > low)
			cnt[a[low++]]--;
		while (q[i].right < high)
			cnt[a[high--]]--;
		while (q[i].right > high)
			cnt[a[++high]]++;
		
		int j;
		for (j = 1; j <= c; j++)
			if (cnt[j] > (high - low + 1) / 2)
				break;

		if (j <= c)
			ans[q[i].index] = j;
	}

	for (int i = 0; i < m; i++) {
		if (ans[i])
			cout << "yes " << ans[i] << '\n';
		else
			cout << "no\n";
	}
}
