#include <bits/stdc++.h>
using namespace std;

bool sieve[2001];
vector<bool> visited;
vector<int> adj[51];
vector<int> matchA, matchB;
vector<int> a_set, b_set;

bool dfs(int a) {
	if (a == 0 || visited[a])
		return false;

	visited[a] = true;
	for (int b : adj[a]) {
		if (matchB[b] == -1 || dfs(matchB[b])) {
			matchA[a] = b;
			matchB[b] = a;
			return true;
		}
	}

	return false;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	memset(sieve, true, sizeof(sieve));
	sieve[0] = sieve[1] = false;

	for (int i = 2; i <= sqrt(2001); i++) {
		if (sieve[i])
			for (int j = 2 * i; j <= 2000; j += i)
				sieve[j] = false;
	}

	int n;
	cin >> n;

	int first_num;
	cin >> first_num;

	bool is_first_even = (first_num % 2 ? false : true);
	a_set.push_back(first_num);

	int temp;
	for (int i = 1; i < n; i++) {
		cin >> temp;

		if (is_first_even)
			if (temp % 2)
				b_set.push_back(temp);
			else
				a_set.push_back(temp);
		else
			if (temp % 2)
				a_set.push_back(temp);
			else
				b_set.push_back(temp);
	}

	if (b_set.size() ^ a_set.size()) {
		cout << -1;
		return 0;
	}

	for (int i = 0; i < a_set.size(); i++)
		for (int j = 0; j < b_set.size(); j++)
			if (sieve[a_set[i] + b_set[j]])
				adj[i].push_back(j);

	vector<int> ans;
	for (int next : adj[0]) {
		int res = 1;

		matchA = vector<int>(a_set.size(), -1);
		matchB = vector<int>(b_set.size(), -1);
		
		matchA[0] = next;
		matchB[next] = 0;

		for (int i = 1; i < a_set.size(); i++) {
			visited = vector<bool>(a_set.size(), false);
			if (dfs(i))
				res++;
		}

		if (res == b_set.size())
			ans.push_back(b_set[next]);
	}

	if (ans.size()) {
		sort(ans.begin(), ans.end());
		for (int i : ans)
			cout << i << ' ';
	}
	else
		cout << -1;
}
