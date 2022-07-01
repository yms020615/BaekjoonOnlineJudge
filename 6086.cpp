#include <bits/stdc++.h>
using namespace std;

const int MAX = 52;
const int inf = 2147483647;
const int SOURCE = 'A' - 'A';
const int SINK = 'Z' - 'A';

int c[MAX][MAX];
int f[MAX][MAX];

int maximumFlow(int source, int sink) {
	int ret = 0;

	while (true) {
		int parent[MAX];
		fill(parent, parent + MAX, -1);

		queue<int> q;
		q.push(source);
		parent[source] = source;

		while (!q.empty() && parent[sink] == -1) {
			int curr = q.front();
			q.pop();

			for (int i = 0; i < MAX; i++) {
				if (c[curr][i] - f[curr][i] > 0 and parent[i] == -1) {
					q.push(i);
					parent[i] = curr;
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

	int n;
	cin >> n;

	char from, to;
	int capa;
	for (int i = 0; i < n; i++) {
		cin >> from >> to >> capa;

		if ('a' <= from and from <= 'z')
			from = from - 'a' + 26;
		else
			from -= 'A';

		if ('a' <= to and to <= 'z')
			to = to - 'a' + 26;
		else
			to -= 'A';

		c[from][to] += capa;
		c[to][from] += capa;
	}

	cout << maximumFlow(SOURCE, SINK);
}
