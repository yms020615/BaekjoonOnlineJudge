#include <iostream>
#include <string>
#include <algorithm>
#define FAST cin.tie(NULL); cout.tie(NULL); ios::sync_with_stdio(false)
using namespace std;

int n, t;
int suffix[500001], lcp[500001], temp[500001], g[500001], tg[500001];
string s;

bool compare(int a, int b) {
    if (g[a] == g[b])
        return g[a+t] < g[b+t];
    return g[a] < g[b];
}

void SuffixArray(string str) {
    t = 1;
    n = str.length();
    for (int i = 0; i < n; i++) {
        suffix[i] = i;
        g[i] = str[i];
    }

    while (t <= n) {
        g[n] = -1;
        sort(suffix, suffix + n, compare);
        tg[suffix[0]] = 0;

        for (int i = 1; i < n; i++)
            if (compare(suffix[i-1], suffix[i]))
                tg[suffix[i]] = tg[suffix[i-1]] + 1;
            else
                tg[suffix[i]] = tg[suffix[i-1]];

        for (int i = 0; i < n; i++)
            g[i] = tg[i];
        t *= 2;
    }
}

int main() {
    FAST;
    int tc, len;
    string s1;
    cin >> tc;
    while (tc--) {
    cin >> len >> s1;
        s = s1 + s1;
        SuffixArray(s);

        int idx;
        for (int i = 0; i < n; i++)
            if (suffix[i] < len) {
                idx = i;
                break;
            }

        int ans = 999999;
        while (suffix[idx] < len)
            ans = min(ans, suffix[idx++]);

        cout << ans << "\n";
    }
}
