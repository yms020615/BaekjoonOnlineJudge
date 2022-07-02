#include <bits/stdc++.h>
using namespace std;

const int MAX = 2005;
const int inf = 2147483647;
const int SOURCE = 1;
const int SINK = 2;
const int NODE_K = 3;

int c[MAX][MAX];
int f[MAX][MAX];
vector<int> adj[MAX];

int maximumFlow(int source, int sink) {
	int ret = 0;

	while (true) {
		int parent[MAX] = {};
		queue<int> q;
		q.push(source);
		parent[source] = source;

		while (!q.empty() && !parent[sink]) {
			int curr = q.front();
			q.pop();

			for (int i = 0; i < adj[curr].size(); i++) {
				int next = adj[curr][i];

				if (c[curr][next] - f[curr][next] > 0 and !parent[next]) {
					q.push(next);
					parent[next] = curr;
				}
			}
		}

		if (!parent[sink])
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

	int n, m, k;
	cin >> n >> m >> k;

	adj[SOURCE].push_back(NODE_K);
	adj[NODE_K].push_back(SOURCE);
	c[SOURCE][NODE_K] = k;

	int w, wNum;
	for (int i = 4; i < n + 4; i++) {
		adj[SOURCE].push_back(i);
		adj[i].push_back(SOURCE);
		adj[NODE_K].push_back(i);
		adj[i].push_back(NODE_K);
		c[SOURCE][i] = 1;
		c[NODE_K][i] = k;

		cin >> w;
		for (int j = 0; j < w; j++) {
			cin >> wNum;
			adj[i].push_back(n + NODE_K + wNum);
			adj[n + NODE_K + wNum].push_back(i);
			c[i][n + NODE_K + wNum] = 1;
		}
	}

	for (int i = n + 4; i < n + m + 4; i++) {
		adj[SINK].push_back(i);
		adj[i].push_back(SINK);
		c[i][SINK] = 1;
	}

	cout << maximumFlow(SOURCE, SINK);
}
