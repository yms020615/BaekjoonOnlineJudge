#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 500;
const int MAX_V = 2 * (MAX_N + 1);
const int S = MAX_V - 2;
const int E = MAX_V - 1;
const int inf = 2147483647;

int c[MAX_V][MAX_V];
int d[MAX_V][MAX_V];
int f[MAX_V][MAX_V];
vector<int> adj[MAX_V];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n, m;
	cin >> n >> m;


	for (int i = 1; i <= n; i++) {
		c[S][i] = 1;
		adj[S].push_back(i);
		adj[i].push_back(S);
	}

	for (int i = 1; i <= m; i++) {
		c[i + MAX_N][E] = 1;
		adj[i + MAX_N].push_back(E);
		adj[E].push_back(i + MAX_N);
	}

	for (int i = 1; i <= n; i++) {
		int work;
		cin >> work;

		for (int j = 1; j <= work; j++) {
			int workNum, cost;
			cin >> workNum >> cost;

			adj[i].push_back(workNum + MAX_N);
			adj[workNum + MAX_N].push_back(i);

			d[i][workNum + MAX_N] = cost;
			d[workNum + MAX_N][i] = -cost;

			c[i][workNum + MAX_N] = 1;
		}
	}

	int result = 0;
	int count = 0;

	while (true) {
		int prev[MAX_V], dist[MAX_V];
		bool inQueue[MAX_V] = {false, };

		queue<int> q;
		fill(prev, prev + MAX_V, -1);
		fill(dist, dist + MAX_V, inf);

		dist[S] = 0;
		inQueue[S] = true;
		q.push(S);

		while (!q.empty()) {
			int curr = q.front();
			q.pop();
			inQueue[curr] = false;

			for (int i = 0; i < adj[curr].size(); i++) {
				int next = adj[curr][i];

				if (c[curr][next] - f[curr][next] > 0 && dist[next] > dist[curr] + d[curr][next]) {
					dist[next] = dist[curr] + d[curr][next];
					prev[next] = curr;
					
					if (!inQueue[next]) {
						q.push(next);
						inQueue[next] = true;
					}
				}
			}
		}

		if (prev[E] == -1)
			break;

		int flow = inf;

		for (int i = E; i != S; i = prev[i])
			flow = min(flow, c[prev[i]][i] - f[prev[i]][i]);

		for (int i = E; i != S; i = prev[i]) {
			result += flow * d[prev[i]][i];
			f[prev[i]][i] += flow;
			f[i][prev[i]] -= flow;
		}

		count++;
	}

	cout << count << '\n' << result;
}
