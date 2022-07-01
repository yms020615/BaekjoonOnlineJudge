#include <bits/stdc++.h>
using namespace std;

const int MAX = 400;
const int inf = 2147483647;
const int SOURCE = 1;
const int SINK = 2;

int c[2 * (MAX + 1)][2 * (MAX + 1)];
int f[2 * (MAX + 1)][2 * (MAX + 1)];
vector<int> adj[2 * (MAX + 1)];

int maximumFlow(int source, int sink) {
	int ret = 0;

	while (true) {
		int parent[2 * (MAX + 1)];
		fill(parent, parent + 2 * (MAX + 1), -1);

		queue<int> q;
		q.push(source);
		parent[source] = source;

		while (!q.empty() && parent[sink] == -1) {
			int curr = q.front();
			q.pop();

			for (int i = 0; i < adj[curr].size(); i++) {
				int next = adj[curr][i];

				if (c[curr][next] - f[curr][next] > 0 and parent[next] == -1) {
					q.push(next);
					parent[next] = curr;
				}
			}
		}

		if (parent[sink] == -1)
			break;

		int flow = inf;
		for (int i = sink; i != source; i = parent[i])
			flow = min(flow, c[parent[i]][i] - f[parent[i]][i]);

		for (int i = sink; i != source; i = parent[i]) {
			f[parent[i]][i] += flow;
			f[i][parent[i]] -= flow;
		}

		ret += flow;
	}

	return ret;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n, p;
	cin >> n >> p;

	for (int i = 1; i <= n; i++) {
		adj[i].push_back(i + MAX);
		adj[i + MAX].push_back(i);

		c[i][i + MAX] = 1;
	}

	int from, to;
	for (int i = 0; i < p; i++) {
		cin >> from >> to;
		adj[from].push_back(to + MAX);
		adj[to + MAX].push_back(from);

		adj[from + MAX].push_back(to);
		adj[to].push_back(from + MAX);

		c[from + MAX][to] = 1;
		c[to + MAX][from] = 1;
	}

	cout << maximumFlow(SOURCE + MAX, SINK);
}
