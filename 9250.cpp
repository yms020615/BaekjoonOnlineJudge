#include <bits/stdc++.h>
using namespace std;

struct Trie {
	Trie *go[26];
	Trie *fail;
	bool output;

	Trie() {
		fill(go, go + 26, nullptr);
		output = false;
	}

	~Trie() {
		for (int i = 0; i < 26; i++)
			if (go[i])
				delete go[i];
	}

	void insert(const char* key) {
		if (*key == 0) {
			output = true;
			return;
		}

		int next = *key - 'a';
		if (!go[next])
			go[next] = new Trie;

		go[next]->insert(key + 1);
	}
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;
	
	char s[10001];
	Trie* root = new Trie;
	for (int i = 0; i < n; i++) {
		cin >> s;
		root->insert(s);
	}

	queue<Trie*> q;
	root->fail = root;
	q.push(root);

	while (!q.empty()) {
		Trie* curr = q.front();
		q.pop();

		for (int i = 0; i < 26; i++) {
			Trie *next = curr->go[i];
			if (!next)
				continue;

			if (curr == root)
				next->fail = root;
			else {
				Trie* dest = curr->fail;

				while (dest != root and !dest->go[i])
					dest = dest->fail;

				if (dest->go[i])
					dest = dest->go[i];
				next->fail = dest;
			}

			if (next->fail->output)
				next->output = true;

			q.push(next);
		}
	}

	int m;
	for (cin >> m; m--;) {
		cin >> s;
		Trie* curr = root;
		bool result = false;

		for (int i = 0; s[i]; i++) {
			int next = s[i] - 'a';

			while (curr != root and !curr->go[next])
				curr = curr->fail;

			if (curr->go[next])
				curr = curr->go[next];

			if (curr->output) {
				result = true;
				break;
			}
		}

		cout << (result ? "YES\n" : "NO\n");
	}

	delete root;
}
