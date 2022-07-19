#include <bits/stdc++.h>

using namespace std;

int SQRT;
int cnt[1000001];
int ccnt[1000001];
int a[100001], ans[100001];
int curr = 0;
pair<pair<int, int>, int> order;

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
		if (cnt[index])
			ccnt[cnt[index]]--;

		cnt[index]++;
		ccnt[cnt[index]]++;
		curr = max(curr, cnt[index]);
	}
	
	else {
		ccnt[cnt[index]]--;
		
		if (cnt[index] == curr and !ccnt[curr])
			curr--;

		cnt[index]--;
		ccnt[cnt[index]]++;
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n;
	cin >> n;
	SQRT = (int)sqrt(n);
	for (int i = 0; i < n; i++)
		cin >> a[i];

	int m;
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> q[i].left >> q[i].right;
		q[i].left--;
		q[i].right--;
		q[i].index = i;
	}

	sort(q, q + m);

	int low = 0, high = 0;
	add_erase(a[0], true);
	for (int i = 0; i < m; i++) {
		auto &next = q[i];
		
		for (int j = low; j < next.left; j++)
			add_erase(a[j], false);
		for (int j = low - 1; j >= next.left; j--)
			add_erase(a[j], true);
		for (int j = high + 1; j <= next.right; j++)
			add_erase(a[j], true);
		for (int j = high; j > next.right; j--)
			add_erase(a[j], false);

		low = next.left;
		high = next.right;
		ans[next.index] = curr;
	}

	for (int i = 0; i < m; i++)
		cout << ans[i] << "\n";
}
